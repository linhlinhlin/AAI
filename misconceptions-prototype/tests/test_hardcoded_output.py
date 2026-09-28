from dataclasses import asdict, replace

import pytest

from misconceptions.ai_labeling import cluster_evidence, interpretation, local_proposal
from misconceptions.domain import Submission
from misconceptions.features import FeatureSpace, extract_oav
from misconceptions.hardcoded_output import LABEL, hardcoded_output
from misconceptions.llm_client import LLMRequestError, request_label
from misconceptions.semantic_rules import diagnose


def row(body):
    return Submission('fixture', 'author', 'sum-range', 'c',
                      '#include <stdio.h>\nint main(){int n;scanf("%d",&n);' + body + 'return 0;}',
                      'v1', {'t1': 'fail', 't2': 'fail', 't3': 'pass'}, 'authored_fixture')


@pytest.mark.parametrize('body', ['printf("%d",5050);', 'printf("15");', 'puts("0");',
                                 'int sum=0;printf("%d",sum);', 'n=15;printf("%d",n);',
                                 'printf("%d",3*5);'])
def test_constant_outputs_are_observed_features_and_rules(body):
    r = row(body)
    assert extract_oav(r)['is_hardcoded_output'] is True
    findings = diagnose(r, [{'test_id': t, 'input': str(i), 'expected': '100', 'output': '0'}
                            for i, t in enumerate(('t1', 't2'))])
    finding = next(f for f in findings if f['rule_id'] == 'C_HARDCODED_OUTPUT')
    assert finding['then_vi'] == LABEL and finding['category'] == 'observed_error'
    assert finding['source'][0]['code'].startswith(('printf', 'puts'))


@pytest.mark.parametrize('body', ['printf("%d",n);', 'printf("%d",n*(n+1)/2);',
                                 'int sum=n;printf("%d",sum);',
                                 'if(n>0)puts("positive");else puts("negative");',
                                 'printf("prompt");printf("%d",n);',
                                 '/* printf("5050"); */ printf("%d",n);',
                                 'for(int i=0;i<n;i++)printf("1");',
                                 'int a=helper();printf("0");',
                                 'printf("%d");', 'return 0;printf("0");'])
def test_dependent_or_unsupported_output_is_not_claimed_hardcoded(body):
    assert not extract_oav(row(body))['is_hardcoded_output']


def test_failures_required_and_diagnostic_does_not_change_frozen_feature_space():
    r = row('printf("0");')
    assert not hardcoded_output(r.source_code, {'t1': 'fail', 't2': 'not_run'})
    assert not hardcoded_output('#define printf custom\n' + r.source_code, r.outcomes)
    s = replace(r, submission_id='other', source_code=row('printf("%d",n);').source_code)
    space = FeatureSpace.fit([r, s], ['t1', 't2', 't3'], feature_mode='combined')
    assert 'is_hardcoded_output' not in space.names  # Diagnostic uses outcomes, not pure AST.


def test_full_raw_code_and_saved_report_reanalysis_and_mixed_coverage():
    r = row('printf("5050");')
    r = replace(r, source_code='/*' + 'padding ' * 700 + '*/\n' + r.source_code)
    report = {'train_assignments': {'fixture': 0}, 'holdout_assignments': {},
              'submissions': [asdict(r)], 'medoids': {'0': 'fixture'}}
    payload, bindings = cluster_evidence(report, [r], {}, 'Sum', 0)
    assert len(payload['samples']) == 1 and bindings == {'sample_1': 'fixture'}
    sample = payload['samples'][0]
    assert sample['raw_code'] == r.source_code and not sample['raw_code_truncated']
    assert sample['hardcoded_output_evidence'] and sample['oav']['is_hardcoded_output']
    local = local_proposal(report, 0, 1)
    assert local['misconception_name'] == LABEL and local['category'] == 'other_error'
    assert interpretation(local, {'misconception_name': 'Không rõ lỗi', 'reasoning': 'Không có dấu hiệu',
                                 'teaching_hint': 'Truy vết input.', 'evidence_samples': []})['misconception_name'] == LABEL
    s = replace(row('printf("%d",n);'), submission_id='other')
    report['submissions'].append(asdict(s))
    report['holdout_assignments']['other'] = 0
    mixed = local_proposal(report, 0, 2)
    assert mixed['category'] == 'mixed' and '1/2' in mixed['reasoning']


def test_raw_code_is_never_silently_truncated(monkeypatch):
    r = replace(row('printf("0");'), source_code='/*' + 'x' * 200_001 + '*/' + row('printf("0");').source_code)
    payload, _ = cluster_evidence({'train_assignments': {'fixture': 0}}, [r], {}, '', 0)
    assert payload['samples'][0]['raw_code'] == r.source_code
    monkeypatch.setattr('urllib.request.urlopen', lambda *_: pytest.fail('Oversized context must not call API'))
    with pytest.raises(LLMRequestError, match='200 KB') as error:
        request_label(payload, {'provider': 'groq', 'model': 'test-model'})
    assert error.value.code == 'context_too_large'

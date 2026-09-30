from copy import deepcopy

from misconceptions.project_reference import attach_reference, load_reference, reference_library


def fixture():
    row = {'submission_id': 'live1', 'problem_id': '2812', 'source_code': 'int main(){}',
           'outcomes': {'1': 'fail'},
           'logged_tests': [{'test_id': '1', 'input': '1', 'expected': 'x', 'output': ''}]}
    record = row | {'case_id': 'case1', 'gold_label': 'Incomplete',
                    'rule': {}, 'reasoning': 'No output', 'source_lines': [1], 'test_ids': ['1']}
    return {'submissions': [row]}, {'records': [record]}


def test_reference_exact_evidence_only_and_does_not_change_features():
    report, reference = fixture()
    original = deepcopy(report['submissions'])
    assert len(attach_reference(report, reference)['confirmed_reference']['matches']) == 1
    assert report['submissions'] == original
    for key, value in [('source_code', 'int main(){return 0;}'), ('problem_id', 'circle-position'),
                       ('outcomes', {'1': 'pass'}), ('logged_tests', [])]:
        changed = {'submissions': [original[0] | {key: value}]}
        assert attach_reference(changed, reference)['confirmed_reference']['matches'] == []


def test_conflicting_reference_abstains_and_missing_file_is_explicit(tmp_path):
    report, reference = fixture()
    reference['records'].append(reference['records'][0] | {'gold_label': 'Other'})
    assert attach_reference(report, reference)['confirmed_reference']['matches'] == []
    assert load_reference(tmp_path / 'missing.json')['status'] == 'unavailable'


def test_confirmed_uncertainty_does_not_become_a_diagnostic_label():
    report, reference = fixture()
    reference['records'][0]['gold_label'] = None
    assert attach_reference(report, reference)['confirmed_reference']['matches'] == []


def test_library_defaults_to_cpack_without_reusing_itsp_approval(monkeypatch, tmp_path):
    import json

    from misconceptions import project_reference

    cluster = {'cluster_id': 'c1', 'problem_id': 'lab02-ex01', 'n_submissions': 4,
               'annotation_status': 'pending_annotation', 'test_statistics': [],
               'semantic_patterns': [], 'representative_sample_ids': [], 'members': []}
    path = tmp_path / 'packet.json'
    path.write_text(json.dumps({'packet_id': 'p1', 'clusters': [cluster]}))
    monkeypatch.setattr(project_reference, 'CPACK_PACKET', path)
    library = reference_library()
    assert library['dataset'] == 'C-Pack-IPAs'
    assert library['human_validated'] is False
    assert library['n_submissions'] == 4
    assert reference_library(cluster_id='c1')['cluster'] == cluster

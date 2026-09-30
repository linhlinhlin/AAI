"""Presentation-only reference labels; never clustering features or independent gold."""

import json
from pathlib import Path

from .ai_labeling import fingerprint

ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / 'deliverables/De5_CPack/gold_reference.json'
ITSP_REFERENCE = ROOT / 'deliverables/De5_Gold_DaXacNhan/gold_reference.json'
CPACK_PACKET = ROOT / 'deliverables/De5_Annotation_20260928/cpack/evidence.json'


def reference_library(source='cpack', cluster_id=None):
    if source == 'cpack_gold':
        return load_reference() | {'dataset': 'C-Pack-IPAs'}
    if source == 'cpack_ai':
        path = ROOT / 'deliverables/De5_CPack/ai_review/nhan_ai.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        if data.get('dataset') != 'C-Pack-IPAs' or data.get('annotation_source') != 'ai':
            raise ValueError('Bản gán nhãn AI không đúng nguồn C-Pack-IPAs.')
        return data
    if source == 'itsp':
        return load_reference(ITSP_REFERENCE) | {'dataset': 'ITSP'}
    if source != 'cpack':
        raise ValueError('Nguồn dữ liệu không hợp lệ.')
    packet = json.loads(CPACK_PACKET.read_text(encoding='utf-8'))
    if cluster_id is not None:
        for cluster in packet['clusters']:
            if cluster['cluster_id'] == cluster_id:
                return {'dataset': 'C-Pack-IPAs', 'packet_id': packet['packet_id'],
                        'cluster': cluster}
        raise ValueError('Không tìm thấy cụm C-Pack-IPAs.')
    fields = ('cluster_id', 'problem_id', 'n_submissions', 'annotation_status',
              'test_statistics', 'semantic_patterns', 'representative_sample_ids')
    return {'dataset': 'C-Pack-IPAs', 'status': 'pending_annotation',
            'human_validated': False, 'packet_id': packet['packet_id'],
            'n_submissions': sum(c['n_submissions'] for c in packet['clusters']),
            'clusters': [{k: c[k] for k in fields} for c in packet['clusters']]}


def evidence_key(row):
    return fingerprint({key: row.get(key) for key in
                        ('problem_id', 'source_code', 'outcomes', 'logged_tests')})


def load_reference(path=None):
    path = path or REFERENCE
    if not path.exists():
        return {'status': 'unavailable', 'records': []}
    data = json.loads(path.read_text(encoding='utf-8'))
    if (data.get('schema_version') != 'project_gold_reference_v1'
            or data.get('annotation_source') != 'ai_proposed_human_confirmed'
            or data.get('status') != 'user_confirmed_project_reference'):
        raise ValueError('Bộ nhãn tham chiếu chưa có định dạng/xác nhận phù hợp.')
    return data


def attach_reference(report, reference=None):
    reference = load_reference() if reference is None else reference
    by_key = {}
    for record in reference['records']:
        if not record.get('gold_label'):
            continue
        by_key.setdefault(evidence_key(record), []).append(record)
    matches = []
    for submission in report.get('submissions', []):
        records = by_key.get(evidence_key(submission), [])
        # Conflicting labels for identical evidence must not be resolved automatically.
        if len({r['gold_label'] for r in records}) != 1:
            continue
        record = records[0]
        matches.append({'submission_id': submission['submission_id'],
                        'case_id': record['case_id'], 'label': record['gold_label'],
                        'rule': record['rule'], 'reasoning': record['reasoning'],
                        'source_lines': record['source_lines'], 'test_ids': record['test_ids']})
    report['confirmed_reference'] = {
        'matches': matches, 'reference_count': len(reference['records']),
        'origin': 'ai_proposed_human_confirmed', 'independent_blind_review': False,
        'matching': 'exact_problem_code_outcomes_and_logs',
    }
    return report

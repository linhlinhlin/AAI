"""Vietnamese project-specific explanation contract; not a diagnostic model."""

STYLE_VERSION = "vi-rule-v1"
TITLES = {
    "C_BRANCH_ATTACHMENT": "Hai nhánh if có thể cùng tạo thông báo",
    "C_SWAP_BY_VALUE": "Hoán vị tham số thường chưa đổi biến ở hàm gọi",
    "OUTPUT_PRESENTATION": "Output khác cách trình bày được yêu cầu",
}
HYPOTHESES = {
    "C_BRANCH_ATTACHMENT": "Có thể người viết nhầm quan hệ if–else và tính loại trừ giữa các nhánh.",
    "C_SWAP_BY_VALUE": "Có thể người viết chưa phân biệt bản sao tham số với biến ở hàm gọi.",
    "OUTPUT_PRESENTATION": "Có thể lỗi nằm ở cách trình bày output; sai khác này chưa cho thấy hiểu sai khái niệm.",
}


def validate_explanation(value):
    fields = {"title", "code_pattern", "behavioral_pattern", "hypothesis", "caveat", "suggested_follow_up"}
    if not isinstance(value, dict) or set(value) != fields:
        raise ValueError("Rule explanation must contain the six vi-rule-v1 fields")
    if not isinstance(value["title"], str) or not value["title"].strip():
        raise ValueError("Rule explanation title must be nonempty")
    for key in fields - {"title"}:
        items = value[key]
        if not isinstance(items, list) or not items or any(
            not isinstance(item, str) or not item.strip() for item in items
        ):
            raise ValueError(f"Rule explanation {key} must be a nonempty list of text")
    if any(not item.startswith("Có thể ") for item in value["hypothesis"]):
        raise ValueError("Hypotheses must begin with 'Có thể '")


def explanation_for(rule_id, conditions, caveat, follow_up):
    value = {"title": TITLES[rule_id], "code_pattern": conditions[:1],
             "behavioral_pattern": conditions[1:], "hypothesis": [HYPOTHESES[rule_id]],
             "caveat": [caveat], "suggested_follow_up": [follow_up]}
    validate_explanation(value)
    return value

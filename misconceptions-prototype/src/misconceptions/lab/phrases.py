"""Vietnamese wording for execution evidence. Every phrase states an observation, not a cause."""

# (attribute, value) -> phrase. Values that carry no information are absent on purpose.
DEVIATION = {
    ("status", "timeout"): "Chạy quá thời gian",
    ("status", "runtime_error"): "Dừng vì lỗi khi chạy",
    ("numbers", "off_by_one"): "Số in ra lệch 1 so với đáp án",
    ("numbers", "truncated"): "Kết quả mất phần thập phân",
    ("numbers", "precision"): "Sai số chữ số sau dấu phẩy",
    ("numbers", "format_only"): "Số đúng nhưng viết khác định dạng",
    ("numbers", "sign"): "Kết quả sai dấu",
    ("numbers", "zero"): "In ra 0 thay vì kết quả",
    ("numbers", "scale"): "Kết quả gấp hoặc bằng một phần đáp án",
    ("numbers", "fewer"): "In thiếu số",
    ("numbers", "more"): "In thừa số",
    ("numbers", "mixed"): "Nhiều số in ra sai theo nhiều cách",
    ("numbers", "other"): "Số in ra khác đáp án",
    ("text", "case_only"): "Chỉ sai chữ hoa, chữ thường",
    ("text", "typo"): "Sai chính tả ở chữ in ra",
    ("text", "missing_words"): "Thiếu chữ so với đáp án",
    ("text", "extra_words"): "In thêm chữ mà đáp án không có",
    ("text", "different"): "Chữ in ra khác đáp án",
    ("whitespace_only", "yes"): "Chỉ khác khoảng trắng hoặc xuống dòng",
    ("newline_end", "missing"): "Thiếu xuống dòng ở cuối",
    ("newline_end", "extra"): "Thừa dòng trống ở cuối",
    ("lines", "fewer"): "In thiếu dòng",
    ("lines", "more"): "In thừa dòng",
    ("prefix", "truncated"): "Chỉ in được phần đầu của đáp án",
    ("prefix", "extended"): "In đúng rồi in thêm phía sau",
    ("prefix", "empty"): "Không in gì",
    ("other_oracle", "yes"): "In ra đáp án của một trường hợp khác",
}
# Most specific first when several phrases describe the same group.
ORDER = ("status", "prefix", "other_oracle", "whitespace_only", "numbers", "text", "newline_end",
         "lines")
# True of almost any wrong output, so they never name a group on their own.
WEAK = {("numbers", "other"), ("numbers", "mixed"), ("text", "different"), ("other_oracle", "yes"),
        ("lines", "fewer"), ("lines", "more")}
OUTCOME = {"pass": "đạt test {}", "fail": "sai test {}", "timeout": "quá thời gian ở test {}",
           "runtime_error": "lỗi khi chạy test {}", "not_run": "chưa chạy test {}"}


def deviation_phrase(attribute, value):
    return DEVIATION.get((attribute, value))


def lower_first(text):
    return text[:1].lower() + text[1:] if text else text


def quoted(name):
    return f"“{name}”"


def test_label(test_id, names):
    name = names.get(test_id)
    return quoted(name) if name else test_id


def condition_phrase(attribute, value, names):
    """One OAV condition as a lower-case clause, or None when it adds nothing for a reader."""
    if attribute.startswith("test:"):
        template = OUTCOME.get(value)
        return template.format(test_label(attribute[5:], names)) if template else None
    if attribute.startswith("dev:"):
        _, test_id, name = attribute.split(":", 2)
        phrase = deviation_phrase(name, value)
        return f"ở test {test_label(test_id, names)}, {lower_first(phrase)}" if phrase else None
    if attribute.startswith("agg:"):
        phrase = deviation_phrase(attribute[4:], value)
        return lower_first(phrase) if phrase else None
    return None

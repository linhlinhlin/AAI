"""Teaching text for AAI Lab: an error-phrased title, one question to ask and one activity.

Each mechanism category from the repair taxonomy has a default; hand-written rules that
know the exercise override the question or the activity with something more specific.
"""

CATEGORY = {
    "LOOP_BOUNDARY": {
        "title": "Sai biên vòng lặp",
        "question": "Với n = 3, vòng lặp đi qua những giá trị nào của i, và có xử lý phần tử cuối không?",
        "activity": "Truy vết vòng lặp trên bảng với n nhỏ; chốt điều kiện “đã xử lý i phần tử” rồi mới chọn < hay <=."},
    "BRANCH_CONDITION": {
        "title": "Sai điều kiện rẽ nhánh",
        "question": "Tại đúng giá trị biên, ví dụ x = 0, điều kiện này đúng hay sai?",
        "activity": "Lập bảng giá trị cho điều kiện với các giá trị biên; so sánh >, >= và cách ghép &&, ||, else."},
    "INITIALIZATION": {
        "title": "Khởi tạo biến sai",
        "question": "Trước khi xét phần tử nào, biến tổng hoặc biến lớn nhất nên mang giá trị gì?",
        "activity": "Phân biệt phần tử trung hòa (0 cho tổng, 1 cho tích) với việc lấy phần tử đầu tiên làm max, min."},
    "COMPUTATION": {
        "title": "Sai biểu thức tính toán",
        "question": "Tính tay biểu thức với một bộ số cụ thể thì được bao nhiêu, còn đề cần bao nhiêu?",
        "activity": "Viết công thức toán trước, dịch từng bước sang C, dùng ngoặc cho rõ thứ tự tính."},
    "NUMERIC_TYPE": {
        "title": "Nhầm kiểu số hoặc phép chia nguyên",
        "question": "Trong C, 7 / 2 và 7 / 2.0 cho kết quả gì?",
        "activity": "Minh họa kiểu của toán hạng quyết định kiểu phép tính; ép kiểu trước phép chia khi cần phần lẻ."},
    "OUTPUT_FORMAT": {
        "title": "Sai đặc tả định dạng khi in",
        "question": "printf(\"%f\") và printf(\"%.2f\") in cùng một giá trị khác nhau thế nào?",
        "activity": "Ôn bảng đặc tả của printf và đối chiếu output mẫu với output của bài từng ký tự."},
    "OUTPUT_TEXT": {
        "title": "Lệch nội dung chữ in ra",
        "question": "Output của em khác đề ở đâu: lời nhắc thừa, dấu câu hay xuống dòng?",
        "activity": "Giải thích chấm tự động so khớp chính xác; chỉ in đúng những gì đề yêu cầu."},
    "INPUT": {
        "title": "Đọc dữ liệu vào sai",
        "question": "scanf trả về gì khi hết dữ liệu hoặc khi định dạng không khớp?",
        "activity": "Minh họa giá trị trả về của scanf và vòng lặp đọc cho đến hết dữ liệu."},
    "STATEMENT_PLACEMENT": {
        "title": "Đặt câu lệnh sai khối",
        "question": "Khi vòng lặp chạy 3 lần, câu lệnh này được thực hiện mấy lần?",
        "activity": "Tô phạm vi từng khối { } và đếm số lần mỗi câu lệnh chạy trên một ví dụ nhỏ."},
    "MISSING_STATEMENT": {
        "title": "Thiếu một bước xử lý",
        "question": "Kể bằng lời các bước thuật toán cần làm; bước nào chưa có trong chương trình?",
        "activity": "Viết giả mã đủ các bước trước khi code, rồi dùng test biên để tìm bước còn thiếu."},
    "EXTRA_STATEMENT": {
        "title": "Thừa bước xử lý",
        "question": "Mỗi câu lệnh trong vòng lặp phục vụ yêu cầu nào của đề?",
        "activity": "Rà code theo đặc tả; bỏ lệnh cập nhật hai lần và lệnh in gỡ lỗi còn sót."},
    "PARAMETER_PASSING": {
        "title": "Nhầm truyền tham số và con trỏ",
        "question": "Ngay sau lời gọi hàm, a và b trong main bằng bao nhiêu?",
        "activity": "Vẽ ô nhớ của main và của hàm; minh họa truyền địa chỉ rồi gán qua *p."},
    "CONTROL_FLOW": {
        "title": "Sai luồng điều khiển",
        "question": "Chương trình dừng ở lần lặp nào khi gặp break hoặc return?",
        "activity": "Truy vết luồng điều khiển với break, continue, return trên một ví dụ nhỏ."},
}

RULE = {
    "SUM_INPUT": {"question": "Với n = 3, chương trình in gì, còn tổng cần in là bao nhiêu?",
                  "activity": "Truy vết 1 + 2 + 3 với một biến cộng dồn; chỉ ra chỗ phải cộng thay vì in lại n."},
    "SUM_SQUARE": {"question": "Với n = 3, n·n bằng bao nhiêu và 1 + 2 + 3 bằng bao nhiêu?",
                   "activity": "So sánh n(n+1)/2 với n·n trên vài giá trị n nhỏ."},
    "SUM_PREVIOUS": {"question": "Công thức đang dùng có cộng số n vào tổng không?",
                     "activity": "Viết tổng 1 + … + n với n = 3 rồi đối chiếu n(n−1)/2 với n(n+1)/2."},
    "COUNT_ZERO": {"question": "Số 0 có phải số dương không, và điều kiện của em có đếm nó không?",
                   "activity": "Lập bảng giá trị cho > 0 và >= 0 với −1, 0 và 1."},
    "MAX_ZERO": {"question": "Nếu mảng toàn số âm, biến lớn nhất khởi tạo bằng 0 sẽ in ra gì?"},
    "ARRAY_LAST": {"question": "Với n = 4, vòng lặp có xét tới phần tử a[3] không?"},
    "CIRCLE_RADIUS": {"question": "Em đang so x² + y² với r hay với r²? Hai đại lượng có cùng đơn vị không?",
                      "activity": "Tính tay với điểm (2, 0) và r = 3: so x² + y² với r và với r²."},
    "SWAP_OVERWRITE": {"question": "Sau lệnh gán đầu tiên, giá trị cũ của *a còn nằm ở đâu không?",
                       "activity": "Truy vết từng lệnh gán trên hai ô nhớ; dùng biến tạm giữ giá trị cũ."},
    "C_HARDCODED_OUTPUT": {"question": "Nếu đổi input, chương trình của em có in kết quả khác không?",
                           "activity": "Chạy với hai input khác nhau; kết quả phải được tính từ dữ liệu vừa đọc."},
    "C_BRANCH_ATTACHMENT": {"question": "Với input bị trượt, những lệnh if nào chạy, và else thuộc về if nào?",
                            "activity": "Vẽ sơ đồ if / else if / else: mỗi input chỉ đi vào đúng một nhánh."},
}


def advice(category, rule_id=None):
    """Question and activity for a category, overridden by what a specific rule knows."""
    base = CATEGORY[category]
    specific = RULE.get(rule_id, {})
    return {"question": specific.get("question", base["question"]),
            "activity": specific.get("activity", base["activity"])}

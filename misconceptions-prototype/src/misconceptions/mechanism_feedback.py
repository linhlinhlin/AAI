"""Teacher-facing wording per mechanism category (hypotheses to check, never diagnoses)."""

FEEDBACK = {
    "LOOP_BOUNDARY": {
        "name": "Biên và điều khiển vòng lặp",
        "hypothesis": "Có thể nhầm phần tử cuối/đầu thuộc hay không thuộc khoảng lặp (< và <=, bắt đầu từ 0 hay 1).",
        "check": "Cho sinh viên liệt kê giá trị biến đếm ở lần lặp đầu và cuối với n = 3.",
        "reteach": "Truy vết vòng lặp trên bảng với n nhỏ; nhấn mạnh bất biến 'đã xử lý i phần tử'.",
    },
    "BRANCH_CONDITION": {
        "name": "Điều kiện rẽ nhánh",
        "hypothesis": "Có thể nhầm biên so sánh hoặc cách kết hợp điều kiện (&&, ||, else).",
        "check": "Hỏi kết quả của điều kiện tại đúng giá trị biên (ví dụ x = 0, x = 10).",
        "reteach": "Lập bảng chân trị cho điều kiện; kiểm tra các giá trị biên trước khi nộp.",
    },
    "INITIALIZATION": {
        "name": "Khởi tạo biến",
        "hypothesis": "Có thể khởi tạo sai giá trị ban đầu của biến tích lũy hoặc giá trị lớn nhất/nhỏ nhất.",
        "check": "Hỏi giá trị đúng của tổng/tích/max khi chưa đọc phần tử nào.",
        "reteach": "Phân biệt phần tử trung hòa (0 cho tổng, 1 cho tích) và khởi tạo max bằng phần tử đầu.",
    },
    "COMPUTATION": {
        "name": "Biểu thức tính toán",
        "hypothesis": "Công thức hoặc độ ưu tiên toán tử chưa khớp với đặc tả.",
        "check": "Cho tính tay biểu thức với một bộ số cụ thể, so với kết quả mong đợi.",
        "reteach": "Viết công thức toán trước, dịch từng bước sang C, dùng ngoặc rõ ràng.",
    },
    "NUMERIC_TYPE": {
        "name": "Kiểu số và chia nguyên",
        "hypothesis": "Có thể cho rằng phép chia hai số nguyên trả về số thực, hoặc chọn sai kiểu dữ liệu.",
        "check": "Hỏi kết quả của 7 / 2 và (float) 7 / 2 trong C.",
        "reteach": "Minh họa quy tắc kiểu của toán hạng quyết định kiểu phép toán; khi nào cần ép kiểu.",
    },
    "OUTPUT_FORMAT": {
        "name": "Đặc tả định dạng in",
        "hypothesis": "Có thể chưa đọc kỹ yêu cầu về số chữ số thập phân, độ rộng hoặc kiểu đặc tả %.",
        "check": "Cho so sánh printf(\"%f\") và printf(\"%.2f\") với cùng một giá trị.",
        "reteach": "Ôn nhanh bảng đặc tả printf; đối chiếu output với mẫu từng ký tự.",
    },
    "OUTPUT_TEXT": {
        "name": "Nội dung văn bản in ra",
        "hypothesis": "Chủ yếu là lệch đặc tả output (lời nhắc thừa, thiếu xuống dòng, sai chữ), không nhất thiết là hiểu sai khái niệm.",
        "check": "Cho chạy lại với đầu vào mẫu và so khớp output từng ký tự với đề.",
        "reteach": "Giải thích cơ chế chấm tự động so khớp chính xác; không in lời nhắc khi đề không yêu cầu.",
    },
    "INPUT": {
        "name": "Đọc dữ liệu vào",
        "hypothesis": "Có thể dùng sai định dạng scanf hoặc cách xử lý hết dữ liệu (EOF).",
        "check": "Hỏi scanf trả về gì khi hết dữ liệu và khi định dạng không khớp.",
        "reteach": "Minh họa giá trị trả về của scanf và vòng lặp đọc đến EOF.",
    },
    "STATEMENT_PLACEMENT": {
        "name": "Vị trí câu lệnh và phạm vi khối",
        "hypothesis": "Có thể đặt câu lệnh sai khối (đặt lại biến trong vòng lặp, in trong vòng lặp).",
        "check": "Hỏi câu lệnh được thực hiện bao nhiêu lần khi vòng lặp chạy 3 lần.",
        "reteach": "Tô màu phạm vi khối { }; truy vết số lần thực hiện từng câu lệnh.",
    },
    "MISSING_STATEMENT": {
        "name": "Thiếu bước xử lý",
        "hypothesis": "Thuật toán thiếu một bước (cập nhật biến, một trường hợp, một nhánh).",
        "check": "Cho liệt kê các bước thuật toán bằng lời trước khi viết code.",
        "reteach": "Viết giả mã đầy đủ các trường hợp; dùng test biên để phát hiện nhánh thiếu.",
    },
    "EXTRA_STATEMENT": {
        "name": "Thừa bước xử lý",
        "hypothesis": "Có câu lệnh thừa (cập nhật hai lần, in gỡ lỗi còn sót).",
        "check": "Hỏi mỗi câu lệnh trong vòng lặp phục vụ yêu cầu nào của đề.",
        "reteach": "Rà soát code theo đặc tả; xóa lệnh in gỡ lỗi trước khi nộp.",
    },
    "PARAMETER_PASSING": {
        "name": "Truyền tham số và con trỏ",
        "hypothesis": "Có thể cho rằng đổi tham số trong hàm sẽ đổi biến ở nơi gọi.",
        "check": "Hỏi giá trị của a, b trong main ngay sau lời gọi hàm hoán vị.",
        "reteach": "Vẽ ô nhớ của main và của hàm; minh họa truyền địa chỉ và gán qua *p.",
    },
    "CONTROL_FLOW": {
        "name": "Luồng điều khiển",
        "hypothesis": "Có thể thoát vòng lặp hoặc hàm quá sớm (break/return) hoặc thiếu điểm thoát.",
        "check": "Hỏi vòng lặp dừng ở lần lặp nào khi gặp break/return.",
        "reteach": "Truy vết luồng điều khiển với break/continue/return trên ví dụ nhỏ.",
    },
}

CAVEAT = ("Đây là giả thuyết cơ chế lỗi mức chương trình, suy ra từ bằng chứng thực thi và "
          "luật học được; không phải chẩn đoán niềm tin của sinh viên. Hãy kiểm tra bằng câu hỏi "
          "ngắn trước khi giảng lại.")

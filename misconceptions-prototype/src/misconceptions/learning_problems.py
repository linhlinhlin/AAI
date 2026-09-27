"""Original formative exercises. Public tests are not a hidden grading benchmark."""

import hashlib
import json


def make_problem(key, title, topic, description, constraints, starter, cases, hints):
    tests = [{'test_id': f't{i}', 'name': name, 'input': inp, 'expected': expected,
              'focus': focus} for i, (name, inp, expected, focus) in enumerate(cases, 1)]
    digest = hashlib.sha256(json.dumps(tests, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    return {'id': key, 'title': title, 'topic': topic, 'description': description,
            'constraints': constraints, 'starter': starter, 'tests': tests, 'hints': hints,
            'suite_version': 'practice-v1-' + digest[:16], 'suite_sha256': digest,
            'language': 'C17', 'origin': 'AAI authored formative exercises',
            'test_policy': 'Tất cả test đều công khai để luyện tập; không phải kỳ thi.'}


PROBLEMS = [
    make_problem('sum-range', 'Tổng từ 1 đến n', 'Vòng lặp · điều kiện biên',
                 'Đọc số nguyên n. In tổng các số nguyên từ 1 đến n. Khi n = 0, tổng bằng 0.',
                 '0 ≤ n ≤ 10000. In một số nguyên, không kèm lời dẫn.',
                 '#include <stdio.h>\n\nint main(void) {\n    int n;\n    scanf("%d", &n);\n    long long sum = 0;\n    // Tính tổng ở đây\n    printf("%lld\\n", sum);\n    return 0;\n}\n',
                 [('Tổng rỗng', '0\n', '0\n', 'Điểm bắt đầu và trường hợp n = 0'),
                  ('Một phần tử', '1\n', '1\n', 'Có tính cả phần tử cuối không?'),
                  ('Hai phần tử', '2\n', '3\n', 'Số lượt lặp'),
                  ('Dãy ngắn', '5\n', '15\n', 'Cộng dồn thay vì ghi đè'),
                  ('Dãy dài', '100\n', '5050\n', 'Giới hạn trên của vòng lặp'),
                  ('Giới hạn đề', '10000\n', '50005000\n', 'Miền giá trị của biến tổng')],
                 ['Viết tay các giá trị i mà vòng lặp ghé qua khi n = 1 và n = 2.',
                  'Tổng cần nhận mỗi số 1, 2, …, n đúng một lần. Kiểm tra khởi tạo và dấu so sánh.']),
    make_problem('mean-two', 'Trung bình hai số', 'Kiểu dữ liệu · phép chia',
                 'Đọc hai số nguyên a, b. In trung bình cộng với đúng hai chữ số sau dấu chấm.',
                 '−1000 ≤ a, b ≤ 1000. Ví dụ 1 2 → 1.50.',
                 '#include <stdio.h>\n\nint main(void) {\n    int a, b;\n    scanf("%d %d", &a, &b);\n    double mean = 0; // Tính trung bình\n    printf("%.2f\\n", mean);\n    return 0;\n}\n',
                 [('Tổng chẵn', '2 4\n', '3.00\n', 'Công thức trung bình'),
                  ('Có phần lẻ', '1 2\n', '1.50\n', 'Kiểu của phép chia trước khi gán'),
                  ('Hai số âm', '-1 -2\n', '-1.50\n', 'Phép chia với số âm'),
                  ('Khác dấu', '-3 4\n', '0.50\n', 'Giữ lại phần thập phân'),
                  ('Hai số không', '0 0\n', '0.00\n', 'Định dạng hai chữ số'),
                  ('Giới hạn', '1000 1000\n', '1000.00\n', 'Miền giá trị')],
                 ['Biến nhận kết quả là double chưa quyết định kiểu của phép tính bên phải.',
                  'So sánh 3 / 2 với 3 / 2.0. Việc đổi kiểu cần xảy ra trước phép chia.']),
    make_problem('max-array', 'Phần tử lớn nhất', 'Mảng · khởi tạo',
                 'Đọc n, rồi n số nguyên. In phần tử lớn nhất của mảng.',
                 '1 ≤ n ≤ 100; −10000 ≤ mỗi phần tử ≤ 10000.',
                 '#include <stdio.h>\n\nint main(void) {\n    int n, a[100];\n    scanf("%d", &n);\n    for (int i = 0; i < n; i++) scanf("%d", &a[i]);\n    int largest = a[0];\n    // Tìm giá trị lớn nhất\n    printf("%d\\n", largest);\n    return 0;\n}\n',
                 [('Một phần tử', '1\n-7\n', '-7\n', 'Khởi tạo từ dữ liệu'),
                  ('Lớn nhất ở đầu', '4\n9 3 2 1\n', '9\n', 'Không bỏ phần tử đầu'),
                  ('Lớn nhất ở cuối', '4\n1 2 3 9\n', '9\n', 'Không bỏ phần tử cuối'),
                  ('Toàn số âm', '3\n-8 -2 -5\n', '-2\n', 'Không giả định max bằng 0'),
                  ('Các số bằng nhau', '3\n4 4 4\n', '4\n', 'So sánh bằng nhau'),
                  ('Có số không', '4\n-1 0 -9 -3\n', '0\n', 'So sánh có dấu')],
                 ['Giá trị lớn nhất ban đầu có chắc thuộc mảng không?',
                  'Theo dõi largest sau mỗi phần tử, đặc biệt với mảng chỉ có số âm.']),
    make_problem('count-positive', 'Đếm số dương', 'Mảng · phân nhánh',
                 'Đọc n và n số nguyên. In số lượng phần tử lớn hơn 0. Số 0 không là số dương.',
                 '1 ≤ n ≤ 100; −1000 ≤ mỗi phần tử ≤ 1000.',
                 '#include <stdio.h>\n\nint main(void) {\n    int n, x, count = 0;\n    scanf("%d", &n);\n    for (int i = 0; i < n; i++) {\n        scanf("%d", &x);\n        // Cập nhật count\n    }\n    printf("%d\\n", count);\n    return 0;\n}\n',
                 [('Chỉ số không', '1\n0\n', '0\n', 'Phân biệt > với ≥'),
                  ('Một số dương', '1\n5\n', '1\n', 'Một phần tử'),
                  ('Toàn số âm', '3\n-1 -2 -3\n', '0\n', 'Điều kiện số dương'),
                  ('Có đủ ba loại', '5\n-2 0 3 0 4\n', '2\n', 'Không đếm số không'),
                  ('Dương ở cuối', '3\n-1 0 2\n', '1\n', 'Duyệt hết mảng'),
                  ('Tất cả dương', '4\n1 2 3 4\n', '4\n', 'Tăng đếm, không ghi đè')],
                 ['Tự phân loại từng phần tử thành âm, bằng 0 hoặc dương.',
                  'Điều kiện tăng count phải đúng duy nhất khi x > 0. Kiểm tra đủ n lượt đọc.']),
    make_problem('swap', 'Hoán vị qua hàm', 'Hàm · con trỏ',
                 'Đọc hai số nguyên a, b. Dùng một hàm hoán vị rồi in b, a theo thứ tự mới.',
                 '−10000 ≤ a, b ≤ 10000. Hai số đầu ra cách nhau bằng khoảng trắng.',
                 '#include <stdio.h>\n\nvoid swap(int *a, int *b) {\n    // Hoán vị hai giá trị được trỏ tới\n}\n\nint main(void) {\n    int a, b;\n    scanf("%d %d", &a, &b);\n    swap(&a, &b);\n    printf("%d %d\\n", a, b);\n    return 0;\n}\n',
                 [('Hai số khác nhau', '2 7\n', '7 2\n', 'Thay đổi biến tại nơi gọi'),
                  ('Hai số bằng nhau', '4 4\n', '4 4\n', 'Trường hợp không lộ lỗi hoán vị'),
                  ('Khác dấu', '-3 5\n', '5 -3\n', 'Bảo toàn cả hai giá trị'),
                  ('Có số không', '0 8\n', '8 0\n', 'Thứ tự cập nhật'),
                  ('Hai số âm', '-2 -9\n', '-9 -2\n', 'Bảo toàn dấu'),
                  ('Giới hạn', '-10000 10000\n', '10000 -10000\n', 'Miền giá trị')],
                 ['Vẽ hai biến của main và địa chỉ mà tham số a, b đang giữ.',
                  'C truyền đối số theo giá trị, kể cả con trỏ. *a và *b cho phép sửa các ô nhớ được trỏ tới.']),
    make_problem('circle-position', 'Điểm và đường tròn', 'Phân nhánh · trường hợp biên',
                 'Đường tròn có tâm tại gốc tọa độ. Đọc x, y, r. In INSIDE, ON hoặc OUTSIDE tùy vị trí điểm.',
                 '−100 ≤ x, y ≤ 100; 1 ≤ r ≤ 100. Các giá trị đều là số nguyên.',
                 '#include <stdio.h>\n\nint main(void) {\n    int x, y, r;\n    scanf("%d %d %d", &x, &y, &r);\n    // So sánh khoảng cách bình phương với bán kính bình phương\n    return 0;\n}\n',
                 [('Tâm đường tròn', '0 0 5\n', 'INSIDE\n', 'Bên trong'),
                  ('Trên biên', '3 4 5\n', 'ON\n', 'Trường hợp bằng nhau'),
                  ('Bên ngoài', '6 0 5\n', 'OUTSIDE\n', 'Khoảng cách lớn hơn bán kính'),
                  ('Tọa độ âm', '-3 -4 5\n', 'ON\n', 'Khoảng cách có bình phương'),
                  ('Trong gần biên', '2 2 3\n', 'INSIDE\n', 'So sánh bình phương'),
                  ('Ngoài theo đường chéo', '4 4 5\n', 'OUTSIDE\n', 'Một và chỉ một kết luận')],
                 ['Ba quan hệ nhỏ hơn, bằng và lớn hơn phải cho đúng một thông báo.',
                  'So sánh x*x + y*y với r*r. Kiểm tra else đang thuộc if nào.']),
]
BY_ID = {problem['id']: problem for problem in PROBLEMS}


def get_problem(key):
    if not isinstance(key, str) or key not in BY_ID:
        raise ValueError('Bài tập không tồn tại.')
    return BY_ID[key]

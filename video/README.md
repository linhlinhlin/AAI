# Video giải thích đề tài 5

Video hình động tiếng Việt, khoảng 8 phút, 1920×1080, 30 fps. Video giải thích toàn bộ đề tài bằng
lời lẽ đơn giản: bài toán, cách làm cũ, dữ liệu đáp án thật, OAV độ lệch, luật chơi đăng ký
trước, các thước đo, kết quả, ứng dụng AAI Lab và các giới hạn. Mọi con số trong video lấy từ
lần chạy test đã đăng ký (`research/runs/mechanism-v1.1-test/`) và từ thống kê benchmark
(`research/runs/mechanism-bench-v1.1/stats.json`). Những hình chỉ để minh họa đều có ghi
"Minh họa".

## Cấu trúc

- `script.json`: lời thoại của 16 cảnh. `show` là chữ hiện trên phụ đề. `say` là cách đọc,
  dùng khi chữ viết khác cách đọc (số, từ tiếng Anh).
- `scripts/make_voice.py`: tạo giọng đọc (edge-tts, `vi-VN-HoaiMyNeural`), mốc thời gian của
  từng từ, `src/timeline.json`, nhạc nền và hai hiệu ứng âm thanh tổng hợp.
- `scripts/capture_app.py`: chụp AAI Lab từ một bản chạy riêng trên cổng 8771 để dùng trong
  cảnh 12.
- `src/`: mã Remotion. `Explainer.tsx` ghép các cảnh và âm thanh. `scenes/` chứa từng cảnh,
  `components/` chứa các thành phần dùng chung.

## Tạo lại

```text
npm install
python scripts/make_voice.py      # cần mạng; clip không đổi lời thì được dùng lại
npx remotion studio               # xem thử và chỉnh
npx remotion render src/index.ts Explainer out/de5_raw.mp4 --jpeg-quality=95
ffmpeg -i out/de5_raw.mp4 -c:v copy -af loudnorm=I=-16:TP=-1.5:LRA=11 -c:a aac -b:a 192k out/de5_giai_thich.mp4
```

Phụ đề khớp với giọng đọc theo từng từ. Chữ hiển thị được căn với các từ được đọc, nên
"89" vẫn sáng đúng lúc giọng đọc nói "tám mươi chín".

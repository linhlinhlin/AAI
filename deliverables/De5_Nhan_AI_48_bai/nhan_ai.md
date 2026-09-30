# Nhãn AI đề xuất — 48 bài

Bản gán nhãn thử cho 48 bài ITSP. Nguồn: AI; chưa được người đánh giá xác nhận, không phải gold standard. Luật dưới đây là lời giải thích do AI viết từ code/log, không phải kết quả vừa chạy thuật toán quy nạp. Không kết luận niềm tin người học. Gói thiếu đề gốc; nhãn phụ thuộc yêu cầu bài cần được đối chiếu lại. Đọc bản này sẽ thấy gợi ý AI, nên không dùng chính lượt đọc này làm chấm mù độc lập.

## Bài 1 · Đề 2833 — Cập nhật biến lặp ngược chiều dừng

`case_09c0e4b691e12f98` · AI đề xuất · có căn cứ code/log

NẾU vòng lặp bắt đầu từ n, kiểm tra i >= 1 nhưng lại tăng i VÀ các test ghi nhận không có output THÌ gợi ý lỗi: Cập nhật biến lặp ngược chiều dừng.

Ở vòng ngoài, i++ làm i đi xa điều kiện dừng thay vì tiến về 0. Lệnh in nằm sau vòng lặp nên không có đường kết thúc bình thường trước khi có thể tràn số nguyên.

**Gợi ý giảng lại:** Cho học viên ghi ra ba giá trị liên tiếp của i và sửa hướng cập nhật.

**Giới hạn:** Log chỉ ghi output rỗng, không đủ kết luận đã timeout hay crash. Không gọi đây là vòng lặp vô hạn xác định vì tràn int có hành vi không xác định.

**Dòng căn cứ:** [7]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6'].

Test 1: input `4`; mong đợi `Number of possible triangles is 13`; thực tế `(rỗng)`.

Test 2: input `1`; mong đợi `Number of possible triangles is 1`; thực tế `(rỗng)`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    int n,c=0,i,j,k,d=0;
    scanf("%d",&n);
    for(i=n;i>=1;i++)
    {
        for(j=i;j>=1;j--)
        {
            for(k=j;k>=1;k--)
            {
                if(j+k>i)
                c++;
                else
                d++;
            }
        }
    }
    printf("Number of possible triangles is %d",c);
    return 0;
}
```

</details>

## Bài 2 · Đề 2833 — Đếm trùng tam giác khi đổi thứ tự ba cạnh

`case_0a9886e56cec5919` · AI đề xuất · có căn cứ code/log

NẾU cả ba cạnh đều được duyệt độc lập từ 1 đến N, không loại hoán vị trùng VÀ N = 4 cho số đếm 34 thay vì 13 trong log THÌ gợi ý lỗi: Đếm trùng tam giác khi đổi thứ tự ba cạnh.

Các bộ cạnh đổi chỗ vẫn đi qua ba vòng lặp và đều được cộng vào tổng. Bộ ba cạnh của cùng một tam giác vì thế bị đếm nhiều lần.

**Gợi ý giảng lại:** Duyệt theo a ≤ b ≤ c rồi kiểm tra điều kiện tam giác; thử liệt kê các bộ khi N = 2.

**Giới hạn:** Nhãn dựa trên cấu trúc duyệt và oracle lịch sử. Gói chấm từng bài thiếu đề gốc; cần đối chiếu quy ước tam giác không phân biệt thứ tự trước khi duyệt nhãn.

**Dòng căn cứ:** [11, 12, 13, 14]. **Test trượt tham chiếu:** ['1', '3', '4', '5', '6'].

Test 1: input `4`; mong đợi `Number of possible triangles is 13`; thực tế `Number of possible triangles is 34`.

Test 3: input `3`; mong đợi `Number of possible triangles is 7`; thực tế `Number of possible triangles is 15`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
int N;
scanf("%d",&N);
int a;
int b;
int c;
int x;
for(x=0,a=1;a<=N;a=a+1){
    for(b=1;b<=N;b=b+1){
        for(c=1;c<=N;c=c+1){
             if((a+b>c)&&(a+c>b)&&(b+c>a)){
         x=x+1;
             }
        }
        
    }
    
}

printf("Number of possible triangles is %d",x);
    
    return 0;
}
```

</details>

## Bài 3 · Đề 2812 — Thiếu ngoặc nhọn {} gom nhóm lệnh và else tương ứng

`case_0acc01a295dbe087` · AI đề xuất · có căn cứ code/log

NẾU if(a<0) chỉ điều khiển một lệnh in, còn các lệnh in thông báo nằm ngoài nhánh VÀ output có cả thông báo âm và dương cho cùng một số THÌ gợi ý lỗi: Thiếu ngoặc nhọn {} gom nhóm lệnh và else tương ứng.

Thụt lề không tạo thành khối lệnh trong C. Khi a khác 0, các dòng in negative và positive vẫn chạy; log số âm cho thấy hai thông báo nối nhau.

**Gợi ý giảng lại:** Gom các lệnh của mỗi nhánh vào dấu ngoặc nhọn và dùng if/else if/else.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [7, 10, 11, 12, 14, 15]. **Test trượt tham chiếu:** ['1', '3', '4', '5', '6'].

Test 1: input `-12`; mong đợi `-12.0000 is negative`; thực tế `-12.0000 is negative-12.0000 is positive`.

Test 3: input `1`; mong đợi `1.0000 is positive`; thực tế ` is negative1.0000 is positive`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main(){
float a;
scanf("%f",&a);
if(a==0)
    printf("input is zero");
    else
    {
        if(a<0)
    printf("%.4f",a);
    printf(" is negative");
    
    printf("%.4f",a);
    printf(" is positive");
    }
	return 0;
}
```

</details>

## Bài 4 · Đề 2833 — Đếm trùng tam giác khi đổi thứ tự ba cạnh

`case_0c6a60962328c1e8` · AI đề xuất · có căn cứ code/log

NẾU cả ba cạnh đều được duyệt độc lập từ 1 đến N, không loại hoán vị trùng VÀ N = 4 cho số đếm 34 thay vì 13 trong log THÌ gợi ý lỗi: Đếm trùng tam giác khi đổi thứ tự ba cạnh.

Các bộ cạnh đổi chỗ vẫn đi qua ba vòng lặp và đều được cộng vào tổng. Bộ ba cạnh của cùng một tam giác vì thế bị đếm nhiều lần.

**Gợi ý giảng lại:** Duyệt theo a ≤ b ≤ c rồi kiểm tra điều kiện tam giác; thử liệt kê các bộ khi N = 2.

**Giới hạn:** Nhãn dựa trên cấu trúc duyệt và oracle lịch sử. Gói chấm từng bài thiếu đề gốc; cần đối chiếu quy ước tam giác không phân biệt thứ tự trước khi duyệt nhãn.

**Dòng căn cứ:** [8, 9, 10, 11]. **Test trượt tham chiếu:** ['1', '3', '4', '5', '6'].

Test 1: input `4`; mong đợi `Number of possible triangles is 13`; thực tế `Number of possible triangles is 34`.

Test 3: input `3`; mong đợi `Number of possible triangles is 7`; thực tế `Number of possible triangles is 15`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    int N,a,b,c,count;
    count=0;
    scanf("%d",&N);
    for(a=1;a<=N;a=a+1){
        for(b=1;b<=N;b=b+1){
            for(c=1;c<=N;c=c+1){
                if ((a+b>c)&&(b+c>a)&&(c+a>b)){
                    count=count+1;
                }
            }
        }
    }
    printf("Number of possible triangles is %d",count);
    return 0;
}
```

</details>

## Bài 5 · Đề 2812 — Chuỗi printf có định dạng nhưng thiếu đối số

`case_129510b9c7f5485c` · AI đề xuất · có căn cứ code/log

NẾU printf có cả %.4f và %d nhưng chỉ truyền một giá trị VÀ test số dương xuất hiện thêm một số nguyên ngoài đáp án THÌ gợi ý lỗi: Chuỗi printf có định dạng nhưng thiếu đối số.

Nhánh số dương thiếu đối số tương ứng với %d. Con số thừa trong log không phải kết quả tính toán hợp lệ của bài.

**Gợi ý giảng lại:** Đối chiếu từng ký hiệu định dạng với từng đối số; bỏ %d nếu đề không yêu cầu.

**Giới hạn:** printf thiếu đối số gây hành vi không xác định; không khẳng định số thừa sẽ luôn giống log.

**Dòng căn cứ:** [7, 11, 15]. **Test trượt tham chiếu:** ['3', '4', '6'].

Test 3: input `1`; mong đợi `1.0000 is positive`; thực tế `1.0000 is positive 7087920`.

Test 4: input `0.0000001`; mong đợi `0.0000 is positive`; thực tế `0.0000 is positive 7087920`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main(){
    float a;
    scanf("%f",&a);
    if(a>0)   {
    printf("%.4f is positive %d",a);    
    }
    else if(a<0)
    {
    printf( "%0.4f is negative",a);    
    }
    else 
    {
    printf("input is zero");    
    }
	
	return 0;
}
```

</details>

## Bài 6 · Đề 2825 — Bỏ sót trường hợp điểm nằm trên đường tròn

`case_16555bff711ec177` · AI đề xuất · có căn cứ code/log

NẾU code chỉ chia thành bên trong và nhánh else bên ngoài VÀ test trên biên bị in thành bên ngoài THÌ gợi ý lỗi: Bỏ sót trường hợp điểm nằm trên đường tròn.

Giá trị bằng 0 của bình phương khoảng cách trừ bình phương bán kính rơi vào else. Hai test trên đường tròn vì vậy nhận thông báo outside.

**Gợi ý giảng lại:** Tách ba trường hợp nhỏ hơn, bằng và lớn hơn.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [7, 8, 10, 11]. **Test trượt tham chiếu:** ['3', '6'].

Test 3: input `3.0 4.0 5.0 7.0 7.0`; mong đợi `Point is on the Circle.`; thực tế `Point is outside the Circle.`.

Test 6: input `0.0 0.0 5.0 3.0 4.0`; mong đợi `Point is on the Circle.`; thực tế `Point is outside the Circle.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    float x,y,r,x1,y1;
    scanf("%f%f%f%f%f",&x,&y,&r,&x1,&y1);
    if((x1-x)*(x1-x)+(y1-y)*(y1-y)-r*r<0)
    printf("Point is inside the Circle.");
    
    else
    printf("Point is outside the Circle.");
    return 0;
}
```

</details>

## Bài 7 · Đề 2812 — Chỉ in giá trị nhập, chưa in kết quả phân loại

`case_216c12a9dde9fca2` · AI đề xuất · có căn cứ code/log

NẾU chương trình đọc số rồi chỉ printf số đó VÀ output thiếu thông báo âm, dương hoặc zero mà oracle yêu cầu THÌ gợi ý lỗi: Chỉ in giá trị nhập, chưa in kết quả phân loại.

Bài đã đọc được dữ liệu nhưng chưa có phần phân loại và in thông báo. Đây không phải lỗi in hằng số: giá trị in vẫn phụ thuộc đầu vào.

**Gợi ý giảng lại:** Bổ sung ba nhánh theo dấu và dùng đúng chuỗi thông báo.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [4, 5]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `-12`; mong đợi `-12.0000 is negative`; thực tế `-12.0000`.

Test 2: input `0`; mong đợi `input is zero`; thực tế `0.0000`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main(){float a;
scanf("%f",&a);
printf("%.4f",a);	
	return 0;
}
```

</details>

## Bài 8 · Đề 2825 — Gắn else vào if thứ hai, khiến một điểm nhận hai kết luận

`case_24cb26b6f2842d5a` · AI đề xuất · có căn cứ code/log

NẾU hai if độc lập kiểm tra trong/ngoài, còn else gắn với if kiểm tra bên ngoài VÀ test điểm bên trong in cả inside và on THÌ gợi ý lỗi: Gắn else vào if thứ hai, khiến một điểm nhận hai kết luận.

Khi điểm ở bên trong, if đầu in inside. if thứ hai sai nên else của nó tiếp tục in on. Cần một chuỗi nhánh loại trừ nhau.

**Gợi ý giảng lại:** Đổi if thứ hai thành else if, rồi truy vết lại một test bên trong.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [13, 14, 15, 16, 17, 18]. **Test trượt tham chiếu:** ['4', '5'].

Test 4: input `3.0 4.0 5.0 5.6 6.2`; mong đợi `Point is inside the Circle.`; thực tế `Point is inside the Circle.Point is on the Circle.`.

Test 5: input `-1.0 -2.0 5.0 1.5 2.0`; mong đợi `Point is inside the Circle.`; thực tế `Point is inside the Circle.Point is on the Circle.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    float x;
    float y;
    float r;
    float x1;
    float y1;
    float n;
    scanf("%f %f %f %f %f",&x,&y,&r,&x1,&y1);
    n=(x-x1)*(x-x1)+(y-y1)*(y-y1)-r*r;
    if ( n < 0 )
    printf("Point is inside the Circle.");
    if ( n > 0 )
    printf("Point is outside the Circle.");
    else
    printf("Point is on the Circle.");
    return 0;
}
```

</details>

## Bài 9 · Đề 2825 — Thiếu địa chỉ biến khi gọi scanf

`case_2abc3cc7bdaf6132` · AI đề xuất · có căn cứ code/log

NẾU scanf dùng %f nhưng truyền giá trị x, y, r, x1, y1 thay cho địa chỉ các biến VÀ các log không ghi nhận output THÌ gợi ý lỗi: Thiếu địa chỉ biến khi gọi scanf.

scanf cần địa chỉ nơi ghi dữ liệu. Lời gọi hiện tại truyền các biến float chưa được nhập thay vì &x, &y, &r, &x1, &y1.

**Gợi ý giảng lại:** Thêm & vào từng biến nhận dữ liệu và giải thích scanf ghi vào đâu.

**Giới hạn:** Lỗi đối số được thấy trực tiếp trong code. Output rỗng không đủ chứng minh crash; lời gọi này có hành vi không xác định.

**Dòng căn cứ:** [6]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `1.2 2.3 2.7 5.3 7.6`; mong đợi `Point is outside the Circle.`; thực tế `(rỗng)`.

Test 2: input `0.0 0.0 5.0 3.0 7.0`; mong đợi `Point is outside the Circle.`; thực tế `(rỗng)`.

<details><summary>Code gốc</summary>

```c
#include <stdio.h>
#include <math.h>

int main(){
    float x, y, r, x1, y1;
    scanf("%f%f%f%f%f",x, y, r, x1, y1);
    float s = sqrt(((x1-x)*(x1-x)) + ((y1-y)*(y1-y)));
    if (s == r){
        printf("Point is on the Circle.");
    }
    else{
        if (s > r){
            printf("Point is outside the Circle.");
        }
        else{
            printf("Point is inside the Circle.");
        }
    }

    return 0;
}
```

</details>

## Bài 10 · Đề 2825 — Thiếu dấu chấm cuối thông báo

`case_2d9e7435a0e0b846` · AI đề xuất · có căn cứ code/log

NẾU chuỗi printf không có dấu chấm cuối câu VÀ output ghi nhận khớp nội dung phân loại nhưng thiếu dấu chấm so với oracle THÌ gợi ý lỗi: Thiếu dấu chấm cuối thông báo.

Khác biệt nhìn thấy trong các test là dấu chấm cuối câu. Không có căn cứ từ sai khác này để kết luận học viên chưa hiểu công thức khoảng cách.

**Gợi ý giảng lại:** Đối chiếu chuỗi output với mẫu, kể cả dấu câu.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [11, 13, 15]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `1.2 2.3 2.7 5.3 7.6`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the Circle`.

Test 2: input `0.0 0.0 5.0 3.0 7.0`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the Circle`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>
#include<math.h>

int main()
{
    float x,y,r,x1,y1,d,e;
    scanf ("%f %f %f %f %f",&x,&y,&r,&x1,&y1);
    d = (x-x1)*(x-x1)+(y-y1)*(y-y1);
    e = sqrt(d);
    if
    (e<r) {printf("Point is inside the Circle");}
    else if
    (e==r) {printf("Point is on the Circle");}
    else if
    (e>r) {printf("Point is outside the Circle");}
    return 0;
}
```

</details>

## Bài 11 · Đề 2833 — Đếm trùng tam giác khi đổi thứ tự ba cạnh

`case_37a5240b3b9aee8e` · AI đề xuất · có căn cứ code/log

NẾU cả ba cạnh đều được duyệt độc lập từ 1 đến N, không loại hoán vị trùng VÀ N = 4 cho số đếm 34 thay vì 13 trong log THÌ gợi ý lỗi: Đếm trùng tam giác khi đổi thứ tự ba cạnh.

Các bộ cạnh đổi chỗ vẫn đi qua ba vòng lặp và đều được cộng vào tổng. Bộ ba cạnh của cùng một tam giác vì thế bị đếm nhiều lần.

**Gợi ý giảng lại:** Duyệt theo a ≤ b ≤ c rồi kiểm tra điều kiện tam giác; thử liệt kê các bộ khi N = 2.

**Giới hạn:** Nhãn dựa trên cấu trúc duyệt và oracle lịch sử. Gói chấm từng bài thiếu đề gốc; cần đối chiếu quy ước tam giác không phân biệt thứ tự trước khi duyệt nhãn.

**Dòng căn cứ:** [6, 8, 10, 11]. **Test trượt tham chiếu:** ['1', '3', '4', '5', '6'].

Test 1: input `4`; mong đợi `Number of possible triangles is 13`; thực tế `Number of possible triangles is 34`.

Test 3: input `3`; mong đợi `Number of possible triangles is 7`; thực tế `Number of possible triangles is 15`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{int n,i,j,k,s=0;
scanf("%d",&n);
for (i=1;i<=n;i=i+1)
{
    for (j=1;j<=n;j=j+1)
    {
        for (k=1;k<=n;k=k+1)
        {if (i+j>k&&i+k>j&&j+k>i)
        {s=s+1;
            
        }
            
            
        }
        
    }
    
    
    
}
    printf("Number of possible triangles is %d",s); 
    return 0;
}
```

</details>

## Bài 12 · Đề 2833 — Dùng điều kiện lọc làm điều kiện dừng vòng lặp (vòng lặp bị ngắt sớm)

`case_476e8d8cdbb2d69f` · AI đề xuất · có căn cứ code/log

NẾU vòng while của cạnh c vừa kiểm tra giới hạn vừa yêu cầu a < c+b ngay từ c=1 VÀ N = 4 chỉ đếm 10 thay vì 13 THÌ gợi ý lỗi: Dùng điều kiện lọc làm điều kiện dừng vòng lặp (vòng lặp bị ngắt sớm).

Một c nhỏ chưa tạo tam giác không có nghĩa các c lớn hơn đều không tạo được. Khi điều kiện sai ngay đầu vòng, code bỏ qua các giá trị c tiếp theo có thể hợp lệ.

**Gợi ý giảng lại:** Duyệt hết c trong giới hạn; đặt điều kiện tam giác bên trong vòng lặp.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [12, 15]. **Test trượt tham chiếu:** ['1', '3', '4', '5'].

Test 1: input `4`; mong đợi `Number of possible triangles is 13`; thực tế `Number of possible triangles is 10`.

Test 3: input `3`; mong đợi `Number of possible triangles is 7`; thực tế `Number of possible triangles is 6`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main(){
    int N,a,b,c,i;
    scanf("%d",&N);
    i=0;
    a=1;b=1;c=1;
   while(a<=N){
       b=1;
       while(b<=a){
           c=1;
            while(c<=b&&a<c+b){
                i=i+1;
                
                c=c+1;
           }
            b=b+1;
       }
        a=a+1;
        
   }

/*Here, N-1 cases must be removed from i because in these cases, a>b+c. And, the number of possible triangles becomes i-(N-1)*/
    printf("Number of possible triangles is %d",i);

    return 0;
}
```

</details>

## Bài 13 · Đề 2812 — In thừa giá trị số ở nhánh zero

`case_4772fe3beb0b26f4` · AI đề xuất · có căn cứ code/log

NẾU nhánh a == 0 in thêm %f trước thông báo VÀ test zero nhận 0.000000 input is zero thay vì input is zero THÌ gợi ý lỗi: In thừa giá trị số ở nhánh zero.

Bài đã đi đúng nhánh zero, nhưng mẫu output của nhánh này không yêu cầu in giá trị a.

**Gợi ý giảng lại:** Giữ nhánh phân loại, sửa chuỗi in riêng cho trường hợp zero.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [7, 9, 10, 13]. **Test trượt tham chiếu:** ['2', '7'].

Test 2: input `0`; mong đợi `input is zero`; thực tế `0.000000 input is zero`.

Test 7: input `0000000`; mong đợi `input is zero`; thực tế `0.000000 input is zero`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main(){
	float a;
	scanf("%f",&a);
	if(a>0)
	    { printf("%.4f is positive",a);
	    }
	 if(a==0)
	    {printf("%f input is zero",a);
	    }
	 if(a<0)
	    {printf("%.4f is negative",a);
	    }
	   
	return 0;
}
```

</details>

## Bài 14 · Đề 2833 — Dùng HOẶC thay cho VÀ và đếm cả các hoán vị cạnh

`case_515052c01c42773f` · AI đề xuất · nhiều cơ chế

NẾU ba bất đẳng thức tam giác nối bằng ||, đồng thời ba cạnh duyệt độc lập VÀ N = 4 cho 64, tức mọi bộ ba đều được đếm THÌ gợi ý lỗi: Dùng HOẶC thay cho VÀ và đếm cả các hoán vị cạnh.

Chỉ cần một bất đẳng thức đúng là code cộng tổng, trong khi điều kiện tam giác cần cả ba. Ngoài ra, miền duyệt hiện tại vẫn đếm các hoán vị như những bộ khác nhau.

**Gợi ý giảng lại:** Sửa || thành && rồi giới hạn thứ tự ba cạnh; kiểm tra từng thay đổi riêng.

**Giới hạn:** Có ít nhất hai cơ chế lỗi cùng hiện diện. Không ép bài này thành nhãn một lỗi duy nhất.

**Dòng căn cứ:** [12, 15, 18, 20]. **Test trượt tham chiếu:** ['1', '3', '4', '5', '6'].

Test 1: input `4`; mong đợi `Number of possible triangles is 13`; thực tế `Number of possible triangles is 64`.

Test 3: input `3`; mong đợi `Number of possible triangles is 7`; thực tế `Number of possible triangles is 27`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    int N;
    int a,b,c;
    a=1;
    b=1;
    c=1;
    int count=0;
    scanf("%d", &N);
    while(a<=N)
    { 
        b=1;
        while(b<=N)
        {
           c=1;
           while(c<=N)
            {
                if(a<b+c||b<a+c||c<a+b)
                {
                    count+=1;
                }
                c+=1;
            }
            b+=1;
        }
        a+=1;
    }
    printf("Number of possible triangles is %d", count);
    return 0;
}
```

</details>

## Bài 15 · Đề 2812 — Kiểm tra một giá trị mẫu thay vì phân loại theo dấu

`case_5507a905e6d6eca8` · AI đề xuất · có căn cứ code/log

NẾU code chỉ xét a == -12 và gọi mọi giá trị còn lại là zero VÀ đầu vào 1 lại được in là zero THÌ gợi ý lỗi: Kiểm tra một giá trị mẫu thay vì phân loại theo dấu.

Điều kiện hiện tại nhận riêng -12 chứ không nhận mọi số âm. Nhánh else cũng gộp cả số dương, số âm khác và số 0.

**Gợi ý giảng lại:** Thay giá trị mẫu bằng điều kiện a < 0, a > 0 và trường hợp còn lại.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [6, 7, 9]. **Test trượt tham chiếu:** ['2', '3', '4', '5', '6', '7'].

Test 2: input `0`; mong đợi `input is zero`; thực tế `0.0000 is zero`.

Test 3: input `1`; mong đợi `1.0000 is positive`; thực tế `1.0000 is zero`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main(){
	float a;
	scanf("%f",&a);
	if (a==-12){
	    printf("%.4f is negative",a);
	} else {
	    printf("%.4f is zero",a);
	}
	return 0;
}
```

</details>

## Bài 16 · Đề 2833 — Bài mới đọc đầu vào, chưa tính và chưa in kết quả

`case_5f142f7662ff032b` · AI đề xuất · có căn cứ code/log

NẾU main chỉ scanf rồi return VÀ mọi test ghi nhận output rỗng THÌ gợi ý lỗi: Bài mới đọc đầu vào, chưa tính và chưa in kết quả.

Không có vòng duyệt, phép đếm hoặc lệnh in nào sau khi đọc N. Có thể đây là bài đang làm dở; chưa thể suy ra học viên hiểu sai khái niệm cụ thể.

**Gợi ý giảng lại:** Yêu cầu viết các bước giải trước, rồi hoàn thiện phần đếm và in.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [6, 8]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6'].

Test 1: input `4`; mong đợi `Number of possible triangles is 13`; thực tế `(rỗng)`.

Test 2: input `1`; mong đợi `Number of possible triangles is 1`; thực tế `(rỗng)`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    int N;
    scanf("%d",&N);
    
    return 0;
}
```

</details>

## Bài 17 · Đề 2825 — Đọc nhầm thứ tự bán kính và tọa độ điểm

`case_5fc7964e49628250` · AI đề xuất · có căn cứ code/log

NẾU scanf gán ba giá trị cuối lần lượt vào x1, y1, r VÀ test 0 0 5 3 7 bị phân loại bên trong thay vì bên ngoài THÌ gợi ý lỗi: Đọc nhầm thứ tự bán kính và tọa độ điểm.

Cách đọc khiến 5 trở thành x1 và 7 trở thành bán kính. Theo thứ tự x, y, r, x1, y1 thể hiện trong bộ test, khoảng cách phải được tính cho điểm (3,7) với bán kính 5.

**Gợi ý giảng lại:** Ghi tên biến ngay dưới từng giá trị của một input mẫu rồi sửa thứ tự scanf.

**Giới hạn:** Cần đối chiếu thứ tự input với đề gốc vì packet này thiếu statement. Bài 17 còn gọi sqrt mà không include math.h; không bỏ qua vấn đề khai báo khi sửa code.

**Dòng căn cứ:** [6, 7]. **Test trượt tham chiếu:** ['1', '2', '3', '5', '6'].

Test 1: input `1.2 2.3 2.7 5.3 7.6`; mong đợi `Point is outside the Circle.`; thực tế `Point is inside the Circle.`.

Test 2: input `0.0 0.0 5.0 3.0 7.0`; mong đợi `Point is outside the Circle.`; thực tế `Point is inside the Circle.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    float x,y,r,x1,y1,s;
    scanf ("%f %f %f %f %f",&x,&y,&x1,&y1,&r);
    s=sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1));
    if  (r >s )
    {
        printf ("Point is inside the Circle.");
        
    }
    else if(r == s)
    {
        printf ("Point is on the Circle."); 
    }
    else
    {
            printf ("Point is outside the Circle.");
    }
    return 0;
}
```

</details>

## Bài 18 · Đề 2825 — Khác chữ hoa/chữ thường trong thông báo

`case_781af59e6dab0a70` · AI đề xuất · có căn cứ code/log

NẾU printf dùng circle với chữ c thường VÀ oracle yêu cầu Circle với chữ C hoa THÌ gợi ý lỗi: Khác chữ hoa/chữ thường trong thông báo.

Sai khác quan sát được là cách viết Circle, không phải vị trí trong/ngoài/trên đường tròn ở các test đã ghi nhận.

**Gợi ý giảng lại:** Đối chiếu từng ký tự của chuỗi thông báo theo mẫu.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [9, 12, 15]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `1.2 2.3 2.7 5.3 7.6`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the circle.`.

Test 2: input `0.0 0.0 5.0 3.0 7.0`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the circle.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    float x, y, r, x1, y1;
    scanf("%f %f %f %f %f", &x, &y, &r, &x1, &y1);
    float dsquared = ((x-x1)*(x-x1)) + ((y-y1)*(y-y1));
    if(dsquared < (r*r)){
        printf("Point is inside the circle.");
    }
    else if(dsquared > (r*r)){
        printf("Point is outside the circle.");
    }
    else{
        printf("Point is on the circle.");
    }
    return 0;
}
```

</details>

## Bài 19 · Đề 2825 — Quên bỏ dòng in debug

`case_78847a573ca84ffd` · AI đề xuất · có căn cứ code/log

NẾU code in khoảng cách kèm chữ demo trước khi in kết luận VÀ output có thêm một dòng không nằm trong đáp án THÌ gợi ý lỗi: Quên bỏ dòng in debug.

Lệnh printf phục vụ kiểm tra tạm vẫn còn trong bài nộp. Ví dụ test đầu in thêm 6.700747 demo trước thông báo outside.

**Gợi ý giảng lại:** Bỏ dòng debug khỏi output nộp bài, giữ lại phần in đáp án.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [13]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `1.2 2.3 2.7 5.3 7.6`; mong đợi `Point is outside the Circle.`; thực tế `6.700747 demo
Point is outside the Circle.`.

Test 2: input `0.0 0.0 5.0 3.0 7.0`; mong đợi `Point is outside the Circle.`; thực tế `7.615773 demo
Point is outside the Circle.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>
#include<math.h>
int main()
{
    float x,y,r;
    float x1;
    float y1;
    float h;
    float g;
    scanf("%f %f %f %f %f",&x,&y,&r,&x1,&y1);/*input*/
    h=(x1-x)*(x1-x)+(y1-y)*(y1-y);
    g=sqrt(h);/*distance formula*/
    printf("%f demo\n",g);
    if(g<r)/*condition for point to be inside the circle*/
    {
        printf("Point is inside the Circle.");
    }
    else if(g==r)/*condition for point to be on the circle*/
    {
        printf("Point is on the Circle.");
    }
    else 
    {
        printf("Point is outside the Circle.");
    }
    return 0;
}
```

</details>

## Bài 20 · Đề 2833 — Sai từ trong mẫu output: triangle thay vì triangles

`case_7e464114951ec19e` · AI đề xuất · có căn cứ code/log

NẾU chuỗi in dùng triangle ở số ít VÀ số đếm trong log khớp oracle nhưng phần chữ thiếu s THÌ gợi ý lỗi: Sai từ trong mẫu output: triangle thay vì triangles.

Không nên gán lỗi đếm tổ hợp cho bài này chỉ vì toàn bộ test fail. Phần số đếm đã khớp ở các test ghi nhận; sai khác nằm ở từ triangles.

**Gợi ý giảng lại:** Giữ phần tính toán và sửa mẫu output theo oracle đã được kiểm chứng.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [20]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6'].

Test 1: input `4`; mong đợi `Number of possible triangles is 13`; thực tế `Number of possible triangle is 13`.

Test 2: input `1`; mong đợi `Number of possible triangles is 1`; thực tế `Number of possible triangle is 1`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    int n,a,b,c,x=0;// x is the no. of triangles formed.a,b,c are sides of                      triangle.n is the input value.
    scanf("%d",&n);
    for(a=1;a<=n;a++)
    {
        for(b=a;b<=n;b++)
        {
            for(c=b;c<=n;c++)
            {
                if((a+b)>c&&(a+c)>b&&(b+c)>a)
                {
                    x++;
                }
            }
        }
    }
    printf("Number of possible triangle is %d",x);
    return 0;
}
```

</details>

## Bài 21 · Đề 2833 — Sai từ trong mẫu output: triangle thay vì triangles

`case_7e5705531d22bbf6` · AI đề xuất · có căn cứ code/log

NẾU chuỗi in dùng triangle ở số ít VÀ số đếm trong log khớp oracle nhưng phần chữ thiếu s THÌ gợi ý lỗi: Sai từ trong mẫu output: triangle thay vì triangles.

Không nên gán lỗi đếm tổ hợp cho bài này chỉ vì toàn bộ test fail. Phần số đếm đã khớp ở các test ghi nhận; sai khác nằm ở từ triangles.

**Gợi ý giảng lại:** Giữ phần tính toán và sửa mẫu output theo oracle đã được kiểm chứng.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [14]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6'].

Test 1: input `4`; mong đợi `Number of possible triangles is 13`; thực tế `Number of possible triangle is 13`.

Test 2: input `1`; mong đợi `Number of possible triangles is 1`; thực tế `Number of possible triangle is 1`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
int i,j,k, N,count=0;
scanf ( "%d",&N);/*input variable*/
for( i=1;i<=N;i=i+1)
{for (j=1 ; j<=i ; j=j+1)
{for (k=1;k<=j; k=k+1)
{if ((j+k>i) && (k+i>j)&& (i+j>k))/*tiangle inequality*/
count++;}
}
}
printf ("Number of possible triangle is %d", count);
    return 0;
}
```

</details>

## Bài 22 · Đề 2825 — Thiếu dấu chấm cuối thông báo

`case_7e6cf30748dd79a5` · AI đề xuất · có căn cứ code/log

NẾU chuỗi printf không có dấu chấm cuối câu VÀ output ghi nhận khớp nội dung phân loại nhưng thiếu dấu chấm so với oracle THÌ gợi ý lỗi: Thiếu dấu chấm cuối thông báo.

Khác biệt nhìn thấy trong các test là dấu chấm cuối câu. Không có căn cứ từ sai khác này để kết luận học viên chưa hiểu công thức khoảng cách.

**Gợi ý giảng lại:** Đối chiếu chuỗi output với mẫu, kể cả dấu câu.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [16, 19, 22]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `1.2 2.3 2.7 5.3 7.6`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the Circle`.

Test 2: input `0.0 0.0 5.0 3.0 7.0`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the Circle`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>
#include<math.h>

int main()
{
    float x, y, r, x1, y1;
    scanf("%f %f %f %f %f",&x,&y,&r,&x1,&y1);
    float A=x-x1;
     float B=y-y1;
    float D,E;
    D=pow(A,2);
    E=pow(B,2);
    float F;
    F=sqrt(D+E);
    if(F>r){
        printf("Point is outside the Circle");
    }
    else if(F<r){
        printf("Point is inside the Circle");
    }
    else{
        printf ("Point is on the Circle");
    };
    return 0;
}
```

</details>

## Bài 23 · Đề 2812 — Thừa dấu chấm so với oracle chấm bài

`case_7fb0598798544be0` · AI đề xuất · có căn cứ code/log

NẾU một hoặc nhiều chuỗi printf có dấu chấm cuối câu VÀ log mong đợi cùng nội dung nhưng không có dấu chấm THÌ gợi ý lỗi: Thừa dấu chấm so với oracle chấm bài.

Các nhánh đang phân loại dấu phù hợp với test; sai khác được trích dẫn là dấu chấm. Bài 33 chỉ thêm dấu chấm ở nhánh dương.

**Gợi ý giảng lại:** Kiểm tra lại mẫu output với người ra đề trước khi yêu cầu sửa dấu câu.

**Giới hạn:** Tài liệu rà soát trước đó ghi nhận ví dụ đề 2812 có dấu chấm nhưng oracle không có. Đây là bất nhất cần kiểm chứng, không phải bằng chứng chắc chắn học viên sai kiến thức.

**Dòng căn cứ:** [7, 9, 11]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `-12`; mong đợi `-12.0000 is negative`; thực tế `-12.0000 is negative.`.

Test 2: input `0`; mong đợi `input is zero`; thực tế `input is zero.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main(){
    float a; // input variable
	scanf("%f",&a);
	  if (a==0)
	    printf ("input is zero.");
	  else if (a>0)
	  printf ("%.4f is positive.",a);
	else
	   printf ("%.4f is negative.",a);
	  
	 
	  
	  
	  
	  
	return 0;
}
```

</details>

## Bài 24 · Đề 2825 — Thiếu dấu chấm cuối thông báo

`case_85d9d4119aeb7f8f` · AI đề xuất · có căn cứ code/log

NẾU chuỗi printf không có dấu chấm cuối câu VÀ output ghi nhận khớp nội dung phân loại nhưng thiếu dấu chấm so với oracle THÌ gợi ý lỗi: Thiếu dấu chấm cuối thông báo.

Khác biệt nhìn thấy trong các test là dấu chấm cuối câu. Không có căn cứ từ sai khác này để kết luận học viên chưa hiểu công thức khoảng cách.

**Gợi ý giảng lại:** Đối chiếu chuỗi output với mẫu, kể cả dấu câu.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [6, 7, 8]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `1.2 2.3 2.7 5.3 7.6`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the Circle`.

Test 2: input `0.0 0.0 5.0 3.0 7.0`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the Circle`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>
int main(){
float a,x,y,r,x1,y1;
scanf("%f%f%f%f%f",&x,&y,&r,&x1,&y1);
a=(x-x1)*(x-x1)+(y-y1)*(y-y1)-r*r ;
if(a==0) {printf("Point is on the Circle");}
else if(a<0){printf("Point is inside the Circle");} 
else {printf("Point is outside the Circle");}                        return 0;
}
```

</details>

## Bài 25 · Đề 2825 — So sánh bình phương khoảng cách với bán kính chưa bình phương

`case_8a259bc637baab56` · AI đề xuất · có căn cứ code/log

NẾU code dùng d² nhưng đối chiếu trực tiếp với r VÀ điểm trên đường tròn bán kính 5 bị báo là ở ngoài THÌ gợi ý lỗi: So sánh bình phương khoảng cách với bán kính chưa bình phương.

Hai vế đang khác đại lượng: d² phải so với r², hoặc d so với r. Ở test 3, d² = 25 và r = 5, nên phép so sánh hiện tại làm lệch kết luận.

**Gợi ý giảng lại:** Cho học viên viết rõ d, d², r, r² rồi chọn một cặp nhất quán.

**Giới hạn:** Bài 46 có tính sqrtf(c) vào d nhưng không dùng d để so sánh, đồng thời thiếu math.h. Nhãn này mô tả sai khác công thức thấy trong code/log, không chứng minh niềm tin của người học.

**Dòng căn cứ:** [6]. **Test trượt tham chiếu:** ['3', '4', '5', '6'].

Test 3: input `3.0 4.0 5.0 7.0 7.0`; mong đợi `Point is on the Circle.`; thực tế `Point is outside the Circle.`.

Test 4: input `3.0 4.0 5.0 5.6 6.2`; mong đợi `Point is inside the Circle.`; thực tế `Point is outside the Circle.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{float x,y,x1,y1,r,s;//s is for power of point
 scanf("%f %f %f %f %f",&x,&y,&r,&x1,&y1);
 s=(x-x1)*(x-x1)+(y-y1)*(y-y1)-r;//computes the power of point
 if(s>0)       //point is outside if s is +ive
  printf("Point is outside the Circle.");
 if(s==0) //point is on it if s=0
  printf("Point is on the Circle.");
 if(s<0)          //point is inside if s is -ive
  printf("Point is inside the Circle.");
 return 0;
}
```

</details>

## Bài 26 · Đề 2833 — Thoát vòng duyệt ngay khi gặp một bộ cạnh chưa hợp lệ

`case_8fc7b8f6d71052ef` · AI đề xuất · có căn cứ code/log

NẾU k đang tăng dần nhưng else lại break khi j+k <= i VÀ số đếm nhỏ hơn oracle, như N = 4 cho 10 thay vì 13 THÌ gợi ý lỗi: Thoát vòng duyệt ngay khi gặp một bộ cạnh chưa hợp lệ.

Một k nhỏ không thỏa chưa loại được những k lớn hơn. break bỏ luôn các bộ phía sau nên bài bị thiếu trường hợp.

**Gợi ý giảng lại:** Bỏ break ở nhánh không hợp lệ và tiếp tục thử các k tiếp theo.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [14, 20]. **Test trượt tham chiếu:** ['1', '3', '4', '5'].

Test 1: input `4`; mong đợi `Number of possible triangles is 13`; thực tế `Number of possible triangles is 10`.

Test 3: input `3`; mong đợi `Number of possible triangles is 7`; thực tế `Number of possible triangles is 6`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    int n;
    int count=0;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=i;j++)
        {
            for(int k=1;k<=j;k++)
            {
                if((j+k)>i)
                {
                    count=count+1;
                }
                else
                {
                    break;
                }
            }
        }
    }
    printf("Number of possible triangles is %d",count);
    return 0;
}
```

</details>

## Bài 27 · Đề 2812 — Đặt biến vào chuỗi định dạng thay vì truyền đối số printf

`case_9055f4a3678ba199` · AI đề xuất · có căn cứ code/log

NẾU chuỗi printf có %.4f và %n nhưng không truyền đối số tương ứng VÀ giá trị in trong log không khớp số đầu vào THÌ gợi ý lỗi: Đặt biến vào chuỗi định dạng thay vì truyền đối số printf.

%n không có nghĩa là in biến tên n; đó là một conversion khác, cần con trỏ để ghi số ký tự đã in. Cả %.4f lẫn %n ở đây đều không có đối số.

**Gợi ý giảng lại:** Đưa n ra sau chuỗi định dạng: printf("%.4f is positive", n), và sửa tương tự nhánh âm.

**Giới hạn:** Lời gọi thiếu đối số có hành vi không xác định. Không suy ra mọi lần chạy đều in 0 từ log lịch sử.

**Dòng căn cứ:** [8, 12, 14]. **Test trượt tham chiếu:** ['1', '3', '4', '5', '6'].

Test 1: input `-12`; mong đợi `-12.0000 is negative`; thực tế `0.0000 is negative,`.

Test 3: input `1`; mong đợi `1.0000 is positive`; thực tế `0.0000 is positive,`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main(){
    //to determine sign of a number
    float n;
    scanf("%f",&n);
    if(n>0){
    printf("%.4f is positive,%n");//number is positive
    }
    else{
        if (n==0){
        printf("input is zero");//number is 0
        }else{
        printf("%.4f is negative,%n");}}//number is negative
    
    
	
	return 0;
}
```

</details>

## Bài 28 · Đề 2812 — Nhầm số 0 với ký tự 0 khi so sánh

`case_90646fdebcac31f8` · AI đề xuất · có căn cứ code/log

NẾU biến số thực được so sánh với '0' thay vì 0 VÀ các test nhập zero không có thông báo THÌ gợi ý lỗi: Nhầm số 0 với ký tự 0 khi so sánh.

'0' là hằng ký tự, không phải giá trị số 0. Khi a bằng 0, hai nhánh >0 và <0 đều sai; điều kiện cuối cũng không nhận đúng zero.

**Gợi ý giảng lại:** Đổi a == '0' thành a == 0 và phân biệt giá trị số với ký tự.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [17]. **Test trượt tham chiếu:** ['2', '7'].

Test 2: input `0`; mong đợi `input is zero`; thực tế `(rỗng)`.

Test 7: input `0000000`; mong đợi `input is zero`; thực tế `(rỗng)`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    float a;
    scanf("%f",&a);
    if(a>0)
    {
        printf("%.4f is positive",a);
    }
    else
    if(a<0)
    {
        printf("%.4f is negative",a);
    }
    else
    if(a=='0')
    {
      printf("input is zero");
    }
	return 0;
}
```

</details>

## Bài 29 · Đề 2812 — Đưa &a vào chuỗi scanf thay vì truyền địa chỉ đối số

`case_917708e5da75df5c` · AI đề xuất · có căn cứ code/log

NẾU lời gọi là scanf("%f,&a") và không có đối số nhận dữ liệu VÀ log không ghi nhận output THÌ gợi ý lỗi: Đưa &a vào chuỗi scanf thay vì truyền địa chỉ đối số.

Phần &a nằm trong dấu nháy nên không cung cấp địa chỉ biến cho %f. Cần viết scanf("%f", &a).

**Gợi ý giảng lại:** Tách chuỗi định dạng khỏi danh sách đối số, rồi kiểm tra giá trị trả về của scanf.

**Giới hạn:** Đây là lỗi đối số trực tiếp; không suy đoán nguyên nhân kết thúc tiến trình chỉ từ output rỗng.

**Dòng căn cứ:** [6]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `-12`; mong đợi `-12.0000 is negative`; thực tế `(rỗng)`.

Test 2: input `0`; mong đợi `input is zero`; thực tế `(rỗng)`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    float a;
    scanf("%f,&a");
    if(a<0.0)
{	printf("%.4f is negative\n",a);}
	if(a==0.0)
{	printf("input is zero");}
	if(a>0.0)
{	printf("%.4f is positive\n",a);}
	return 0;
}
```

</details>

## Bài 30 · Đề 2825 — Tính độ lệch vị trí nhưng lại rẽ nhánh theo bán kính

`case_9f89199d80d76687` · AI đề xuất · có căn cứ code/log

NẾU code tính k = d² − r² rồi dùng dấu của r trong if VÀ cả điểm bên trong và trên biên đều bị in là bên ngoài khi r dương THÌ gợi ý lỗi: Tính độ lệch vị trí nhưng lại rẽ nhánh theo bán kính.

Bán kính dương không cho biết điểm đang ở trong hay ngoài. Biến k đã tính đúng đại lượng cần xét nhưng bị bỏ qua khi rẽ nhánh.

**Gợi ý giảng lại:** Thay biến được kiểm tra từ r sang k và truy vết một điểm bên trong.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [7, 8, 12, 16]. **Test trượt tham chiếu:** ['3', '4', '5', '6'].

Test 3: input `3.0 4.0 5.0 7.0 7.0`; mong đợi `Point is on the Circle.`; thực tế `Point is outside the Circle.`.

Test 4: input `3.0 4.0 5.0 5.6 6.2`; mong đợi `Point is inside the Circle.`; thực tế `Point is outside the Circle.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
float x,y,r,x1,y1,k;
scanf("%f %f %f %f %f",&x,&y,&r,&x1,&y1);
k=(x-x1)*(x-x1)+(y-y1)*(y-y1)-(r*r);
if(r>0){
    printf("Point is outside the Circle.");
    }
else
if(r==0){
    printf("Point is on the Circle.");
}
else
if(r<0){
    printf("Point is inside the Circle.");
}
    // Fill this area with your code.
    return 0;
}
```

</details>

## Bài 31 · Đề 2825 — Thiếu dấu chấm cuối thông báo

`case_a64d890ffd811174` · AI đề xuất · có căn cứ code/log

NẾU chuỗi printf không có dấu chấm cuối câu VÀ output ghi nhận khớp nội dung phân loại nhưng thiếu dấu chấm so với oracle THÌ gợi ý lỗi: Thiếu dấu chấm cuối thông báo.

Khác biệt nhìn thấy trong các test là dấu chấm cuối câu. Không có căn cứ từ sai khác này để kết luận học viên chưa hiểu công thức khoảng cách.

**Gợi ý giảng lại:** Đối chiếu chuỗi output với mẫu, kể cả dấu câu.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [7, 10, 13]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `1.2 2.3 2.7 5.3 7.6`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the Circle`.

Test 2: input `0.0 0.0 5.0 3.0 7.0`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the Circle`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>
int main() {
   float x,y,r,x1,y1;
   scanf("%f %f %f %f %f",&x,&y,&r,&x1,&y1);
   float A=((x-x1)*(x-x1)+(y-y1)*(y-y1));   
 if(A<r*r){
     printf("Point is inside the Circle");
 }
 if(A==r*r){
     printf("Point is on the Circle");
 }    
 if(A>r*r){
     printf("Point is outside the Circle");
 }
   return 0;
}
```

</details>

## Bài 32 · Đề 2825 — Thiếu dấu chấm cuối thông báo

`case_a6f61d6bf5e9e4f8` · AI đề xuất · có căn cứ code/log

NẾU chuỗi printf không có dấu chấm cuối câu VÀ output ghi nhận khớp nội dung phân loại nhưng thiếu dấu chấm so với oracle THÌ gợi ý lỗi: Thiếu dấu chấm cuối thông báo.

Khác biệt nhìn thấy trong các test là dấu chấm cuối câu. Không có căn cứ từ sai khác này để kết luận học viên chưa hiểu công thức khoảng cách.

**Gợi ý giảng lại:** Đối chiếu chuỗi output với mẫu, kể cả dấu câu.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [11, 14, 17]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `1.2 2.3 2.7 5.3 7.6`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the Circle`.

Test 2: input `0.0 0.0 5.0 3.0 7.0`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the Circle`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>
#include<math.h>
int main()
{
    float x,y,r,x1,y1;
    float d,D;/*d=distance squared*/
    scanf("%f%f%f%f%f",&x,&y,&r,&x1,&y1);
    d=((x-x1)*(x-x1))+((y-y1)*(y-y1));/*distance squared*/
    D=sqrtf(d);
    if (D<r){
        printf("Point is inside the Circle");
    }
    if (D==r){
        printf("Point is on the Circle");
    }
    if (D>r){
        printf("Point is outside the Circle");
    }
    return 0;
}
```

</details>

## Bài 33 · Đề 2812 — Thừa dấu chấm so với oracle chấm bài

`case_a7b282a588ab29a3` · AI đề xuất · có căn cứ code/log

NẾU một hoặc nhiều chuỗi printf có dấu chấm cuối câu VÀ log mong đợi cùng nội dung nhưng không có dấu chấm THÌ gợi ý lỗi: Thừa dấu chấm so với oracle chấm bài.

Các nhánh đang phân loại dấu phù hợp với test; sai khác được trích dẫn là dấu chấm. Bài 33 chỉ thêm dấu chấm ở nhánh dương.

**Gợi ý giảng lại:** Kiểm tra lại mẫu output với người ra đề trước khi yêu cầu sửa dấu câu.

**Giới hạn:** Tài liệu rà soát trước đó ghi nhận ví dụ đề 2812 có dấu chấm nhưng oracle không có. Đây là bất nhất cần kiểm chứng, không phải bằng chứng chắc chắn học viên sai kiến thức.

**Dòng căn cứ:** [7, 9, 11]. **Test trượt tham chiếu:** ['3', '4', '6'].

Test 3: input `1`; mong đợi `1.0000 is positive`; thực tế `1.0000 is positive.`.

Test 4: input `0.0000001`; mong đợi `0.0000 is positive`; thực tế `0.0000 is positive.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main(){
	float input; 
	scanf("%f",&input);
	if(input==0)  /** if for 3 possible cases(either > , 0 , = 0) **/
	  {printf("input is zero");}
	else if(input > 0)
	  {printf("%.4f is positive.",input);} /** .4f for 4 digit decimal place **/
	else if(input < 0)
	  {printf("%.4f is negative" ,input);}
	return 0;
}
```

</details>

## Bài 34 · Đề 2825 — Gõ sai Circle thành Cicle ở nhánh bên ngoài

`case_a894cae81674bc6b` · AI đề xuất · có căn cứ code/log

NẾU printf của nhánh outside viết Cicle VÀ test bên ngoài khác oracle đúng một chữ r THÌ gợi ý lỗi: Gõ sai Circle thành Cicle ở nhánh bên ngoài.

Log vẫn cho kết luận outside nhưng thông báo bị sai chính tả. Chưa có căn cứ coi đây là lỗi công thức hình học.

**Gợi ý giảng lại:** Sửa đúng chuỗi mẫu và kiểm tra cả ba nhánh in.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [13, 14, 16]. **Test trượt tham chiếu:** ['1', '2', '7'].

Test 1: input `1.2 2.3 2.7 5.3 7.6`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the Cicle.`.

Test 2: input `0.0 0.0 5.0 3.0 7.0`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the Cicle.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>
#include<math.h>

int main()
{
    float x,y,r,x1,y1;
    scanf("%f %f %f %f %f",&x,&y,&r,&x1,&y1);//input x,y,r,x1,y1
    
    float d=sqrtf((x1-x)*(x1-x)+(y1-y)*(y1-y));
    //compute distance between point and centre of circle
    
    if ((d==r)||(d<r)) {
        if (d==r) printf("Point is on the Circle.");
        else printf("Point is inside the Circle.");
    } else {
        printf("Point is outside the Cicle.");
    }    
    
    return 0;
}
```

</details>

## Bài 35 · Đề 2833 — Dấu chấm phẩy sau for làm thân vòng lặp rỗng

`case_af057346e20493c4` · AI đề xuất · có căn cứ code/log

NẾU mỗi câu for kết thúc ngay bằng dấu ; trước khối ngoặc nhọn VÀ nhiều input khác nhau đều chỉ cho số đếm 1 THÌ gợi ý lỗi: Dấu chấm phẩy sau for làm thân vòng lặp rỗng.

Khối đếm phía dưới không còn là thân của các vòng for. Nó chỉ chạy sau khi các vòng rỗng đã kết thúc, nên không duyệt từng bộ cạnh như dự định.

**Gợi ý giảng lại:** Bỏ dấu ; sau for rồi chỉ rõ khối lệnh thuộc từng vòng.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [8, 10, 12]. **Test trượt tham chiếu:** ['1', '3', '4', '5', '6'].

Test 1: input `4`; mong đợi `Number of possible triangles is 13`; thực tế `Number of possible triangles is 1`.

Test 3: input `3`; mong đợi `Number of possible triangles is 7`; thực tế `Number of possible triangles is 1`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{ int N;
int i,j,k;
 int count=0; 
 scanf("%d",&N);
  for (i=1; i<=N; i++);  
  {
      for (j=i; j<=N; j=j+1);
     {
         for (k=j; k<=N; k=k+1);
     {     if (i+j>k && j+k>i && i+k>j)
     count=count+1;
     }
     }
  } 
  printf ("Number of possible triangles is %d",count);
    return 0;
}
```

</details>

## Bài 36 · Đề 2812 — Thừa dấu chấm so với oracle chấm bài

`case_be7e62b451ca8f22` · AI đề xuất · có căn cứ code/log

NẾU một hoặc nhiều chuỗi printf có dấu chấm cuối câu VÀ log mong đợi cùng nội dung nhưng không có dấu chấm THÌ gợi ý lỗi: Thừa dấu chấm so với oracle chấm bài.

Các nhánh đang phân loại dấu phù hợp với test; sai khác được trích dẫn là dấu chấm. Bài 33 chỉ thêm dấu chấm ở nhánh dương.

**Gợi ý giảng lại:** Kiểm tra lại mẫu output với người ra đề trước khi yêu cầu sửa dấu câu.

**Giới hạn:** Tài liệu rà soát trước đó ghi nhận ví dụ đề 2812 có dấu chấm nhưng oracle không có. Đây là bất nhất cần kiểm chứng, không phải bằng chứng chắc chắn học viên sai kiến thức.

**Dòng căn cứ:** [8, 12, 16]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `-12`; mong đợi `-12.0000 is negative`; thực tế `-12.0000 is negative.`.

Test 2: input `0`; mong đợi `input is zero`; thực tế `input is zero.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main(){
    float a;
    scanf("%f",&a);
    if(a>0)
    {
        printf("%.4f is positive.",a);
    }
	else if(a==0)
	{
	    printf("input is zero.");
	}
	else
	{
	    printf("%.4f is negative.",a);
	}
	return 0;
}
```

</details>

## Bài 37 · Đề 2833 — Sai từ trong mẫu output: triangle thay vì triangles

`case_c3e32b1a7204496b` · AI đề xuất · có căn cứ code/log

NẾU chuỗi in dùng triangle ở số ít VÀ số đếm trong log khớp oracle nhưng phần chữ thiếu s THÌ gợi ý lỗi: Sai từ trong mẫu output: triangle thay vì triangles.

Không nên gán lỗi đếm tổ hợp cho bài này chỉ vì toàn bộ test fail. Phần số đếm đã khớp ở các test ghi nhận; sai khác nằm ở từ triangles.

**Gợi ý giảng lại:** Giữ phần tính toán và sửa mẫu output theo oracle đã được kiểm chứng.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [15]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6'].

Test 1: input `4`; mong đợi `Number of possible triangles is 13`; thực tế `Number of possible triangle is 13`.

Test 2: input `1`; mong đợi `Number of possible triangles is 1`; thực tế `Number of possible triangle is 1`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    int n,c=0,x,y,z;
    scanf("%d",&n);
    for(x=1;x<=n;x=x+1){
     for(y=1;y<=x;y=y+1){
     for(z=1;z<=y;z=z+1){
          if(x+y>z && y+z>x && z+x>y)
     c++;
    }   
     }
    }
    printf("Number of possible triangle is %d",c);
    return 0;

}
```

</details>

## Bài 38 · Đề 2825 — Gắn else vào if thứ hai, khiến một điểm nhận hai kết luận

`case_cc63868c9ce23567` · AI đề xuất · có căn cứ code/log

NẾU hai if độc lập kiểm tra trong/ngoài, còn else gắn với if kiểm tra bên ngoài VÀ test điểm bên trong in cả inside và on THÌ gợi ý lỗi: Gắn else vào if thứ hai, khiến một điểm nhận hai kết luận.

Khi điểm ở bên trong, if đầu in inside. if thứ hai sai nên else của nó tiếp tục in on. Cần một chuỗi nhánh loại trừ nhau.

**Gợi ý giảng lại:** Đổi if thứ hai thành else if, rồi truy vết lại một test bên trong.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [12, 13, 14, 15, 16, 17]. **Test trượt tham chiếu:** ['4', '5'].

Test 4: input `3.0 4.0 5.0 5.6 6.2`; mong đợi `Point is inside the Circle.`; thực tế `Point is inside the Circle.Point is on the Circle.`.

Test 5: input `-1.0 -2.0 5.0 1.5 2.0`; mong đợi `Point is inside the Circle.`; thực tế `Point is inside the Circle.Point is on the Circle.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>
#include<math.h>
int main()
{
  float x, y, r, x1, y1, d;
  scanf("%f",&x);
  scanf("%f",&y);
  scanf("%f",&r);
  scanf("%f",&x1);
  scanf("%f",&y1);
  d =sqrt(pow(x-x1, 2)+pow(y-y1, 2));
  if (d<r){
  printf("Point is inside the Circle.");}
  if (d>r){
  printf("Point is outside the Circle.");}
  else {
  printf("Point is on the Circle.");}
 
    return 0;
}
```

</details>

## Bài 39 · Đề 2825 — Đọc nhầm thứ tự bán kính và tọa độ điểm

`case_cc772f29ff77aae8` · AI đề xuất · có căn cứ code/log

NẾU scanf gán ba giá trị cuối lần lượt vào x1, y1, r VÀ test 0 0 5 3 7 bị phân loại bên trong thay vì bên ngoài THÌ gợi ý lỗi: Đọc nhầm thứ tự bán kính và tọa độ điểm.

Cách đọc khiến 5 trở thành x1 và 7 trở thành bán kính. Theo thứ tự x, y, r, x1, y1 thể hiện trong bộ test, khoảng cách phải được tính cho điểm (3,7) với bán kính 5.

**Gợi ý giảng lại:** Ghi tên biến ngay dưới từng giá trị của một input mẫu rồi sửa thứ tự scanf.

**Giới hạn:** Cần đối chiếu thứ tự input với đề gốc vì packet này thiếu statement. Bài 17 còn gọi sqrt mà không include math.h; không bỏ qua vấn đề khai báo khi sửa code.

**Dòng căn cứ:** [6, 7, 13]. **Test trượt tham chiếu:** ['1', '2', '3', '5', '6'].

Test 1: input `1.2 2.3 2.7 5.3 7.6`; mong đợi `Point is outside the Circle.`; thực tế `Point is inside the Circle.`.

Test 2: input `0.0 0.0 5.0 3.0 7.0`; mong đợi `Point is outside the Circle.`; thực tế `Point is inside the Circle.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>
#include<math.h>
int main()
{
    float x,y,x1,y1,r;
    scanf("%f %f %f %f %f",&x,&y,&x1,&y1,&r);
    if(r==sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1))) 
{    
    printf("Point is on the Circle.");
}
else
{
    if(r<sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1)))
    printf("Point is outside the Circle."); 
    else 
    printf("Point is inside the Circle.");
        
    }
    // Fill this area with your code.
    return 0;
}
```

</details>

## Bài 40 · Đề 2833 — Khử trùng số đếm bằng một công thức không phù hợp

`case_d206b331ed6efff9` · AI đề xuất · có căn cứ code/log

NẾU code đếm các hoán vị rồi thay tổng bằng ((count-n)/n)+n VÀ N = 4 cho 11 thay vì 13 dù một vài input nhỏ vẫn đúng THÌ gợi ý lỗi: Khử trùng số đếm bằng một công thức không phù hợp.

Số hoán vị không cố định theo n: ba cạnh khác nhau, hai cạnh bằng nhau và ba cạnh bằng nhau có số lần lặp khác nhau. Chia tổng theo n không loại trùng đúng cho mọi trường hợp.

**Gợi ý giảng lại:** Giới hạn thứ tự ba cạnh ngay trong vòng duyệt thay vì sửa tổng bằng công thức này.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [7, 9, 11, 20]. **Test trượt tham chiếu:** ['1', '4', '5'].

Test 1: input `4`; mong đợi `Number of possible triangles is 13`; thực tế `Number of possible triangles is 11`.

Test 4: input `5`; mong đợi `Number of possible triangles is 22`; thực tế `Number of possible triangles is 17`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    int n,count=0,a,b,c;
    scanf("%d",&n);
    for(a=1;a<=n;a++)
    {
        for(b=1;b<=n;b++)
        {
            for(c=1;c<=n;c++)
            {
               if((a+b)>c && (a+c)>b && (b+c)>a)
               {
                   count++;
               }
            }
        }
    }
    count=(((count-n)/n)+n);
    printf("Number of possible triangles is %d",count);
    return 0;
}
```

</details>

## Bài 41 · Đề 2825 — Thiếu dấu chấm riêng ở nhánh trên đường tròn

`case_da6a96c98b77ce1a` · AI đề xuất · có căn cứ code/log

NẾU nhánh on in chuỗi không có dấu chấm cuối VÀ chỉ các test trên biên khác oracle ở dấu câu THÌ gợi ý lỗi: Thiếu dấu chấm riêng ở nhánh trên đường tròn.

Bài đã nhận đúng trường hợp trên đường tròn trong log. Lỗi quan sát được nằm ở chuỗi thông báo của nhánh đó.

**Gợi ý giảng lại:** Sửa chuỗi on cho thống nhất với mẫu, không đổi công thức khi chưa có bằng chứng cần đổi.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [14, 17, 20]. **Test trượt tham chiếu:** ['3', '6'].

Test 3: input `3.0 4.0 5.0 7.0 7.0`; mong đợi `Point is on the Circle.`; thực tế `Point is on the Circle`.

Test 6: input `0.0 0.0 5.0 3.0 4.0`; mong đợi `Point is on the Circle.`; thực tế `Point is on the Circle`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>
#include<math.h>

int main()
{
    float x , y , x1 , y1 , r ,s ;
    // (x,y) are co-ordinates for center of circle .
    // (x1,y1) is point whose relative loacation w.r.t circle we have to see .
    // r is radius of circle .
    // s is distance of point from center of circle .
    scanf ("%f %f %f %f %f",&x,&y,&r,&x1,&y1);
    s = sqrtf(((x - x1)*(x - x1)) + ((y - y1)*(y - y1))) ;
    if (s>r){
        printf("Point is outside the Circle.");// if radius is less than distance from center , point is outside the circle .
    }
    else if (s==r){
        printf("Point is on the Circle");// if radius is equal to distance from center , point is on the circumference .
    }
    else{
        printf("Point is inside the Circle.");
        
    }
    // if radius is greater than distance from center then point is inside the circle .
    
    
    return 0;
}
```

</details>

## Bài 42 · Đề 2825 — Nhánh bên ngoài in nhầm thông báo trên đường tròn

`case_e0a24174dbc0a491` · AI đề xuất · có căn cứ code/log

NẾU else sau l<0 và l==0 vẫn in on VÀ test điểm bên ngoài bị báo là nằm trên đường tròn THÌ gợi ý lỗi: Nhánh bên ngoài in nhầm thông báo trên đường tròn.

Cấu trúc đã dành nhánh cuối cho l>0, nhưng chuỗi in bị lặp từ nhánh l==0. Có thể là lỗi sao chép; chưa đủ căn cứ kết luận học viên không hiểu hình học.

**Gợi ý giảng lại:** Đổi thông báo trong else thành outside và kiểm tra một test bên ngoài.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [10, 11, 13, 15, 16]. **Test trượt tham chiếu:** ['1', '2', '7'].

Test 1: input `1.2 2.3 2.7 5.3 7.6`; mong đợi `Point is outside the Circle.`; thực tế `Point is on the Circle.`.

Test 2: input `0.0 0.0 5.0 3.0 7.0`; mong đợi `Point is outside the Circle.`; thực tế `Point is on the Circle.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    float x,y,r,x1,y1,l;
    scanf("%f %f %f %f %f",&x,&y,&r,&x1,&y1);
    l=(x-x1)*(x-x1)+(y-y1)*(y-y1)-(r*r);
    if(l<0)
    {
      printf("Point is inside the Circle.");}
      else if(l==0)
      {
      printf("Point is on the Circle.");
      }
    else
    printf("Point is on the Circle.");
    return 0;
}
```

</details>

## Bài 43 · Đề 2825 — Khác chữ hoa/chữ thường trong thông báo

`case_e15cd0218127818c` · AI đề xuất · có căn cứ code/log

NẾU printf dùng circle với chữ c thường VÀ oracle yêu cầu Circle với chữ C hoa THÌ gợi ý lỗi: Khác chữ hoa/chữ thường trong thông báo.

Sai khác quan sát được là cách viết Circle, không phải vị trí trong/ngoài/trên đường tròn ở các test đã ghi nhận.

**Gợi ý giảng lại:** Đối chiếu từng ký tự của chuỗi thông báo theo mẫu.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [11, 15, 19]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `1.2 2.3 2.7 5.3 7.6`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the circle.`.

Test 2: input `0.0 0.0 5.0 3.0 7.0`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the circle.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>
#include<math.h>
int main()
{
    float x,y,r,x1,y1;
    scanf("%f %f %f %f %f",&x,&y,&r,&x1,&y1);
    float m=(x-x1)*(x-x1)+(y-y1)*(y-y1);
    float d=sqrtf(m);
    if(d==r)
    {
        printf("Point is on the circle.");
    }
    else if(d>r)
        {
            printf("Point is outside the circle.");
        }
    else if(d<r)
        {
            printf("Point is inside the circle.");
        }
    return 0;
}
```

</details>

## Bài 44 · Đề 2825 — Khác chữ hoa/chữ thường trong thông báo

`case_e707d929e1330208` · AI đề xuất · có căn cứ code/log

NẾU printf dùng circle với chữ c thường VÀ oracle yêu cầu Circle với chữ C hoa THÌ gợi ý lỗi: Khác chữ hoa/chữ thường trong thông báo.

Sai khác quan sát được là cách viết Circle, không phải vị trí trong/ngoài/trên đường tròn ở các test đã ghi nhận.

**Gợi ý giảng lại:** Đối chiếu từng ký tự của chuỗi thông báo theo mẫu.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [12, 15, 19]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `1.2 2.3 2.7 5.3 7.6`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the circle.`.

Test 2: input `0.0 0.0 5.0 3.0 7.0`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the circle.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    float x,y,r,x1,y1,a,b,c;
    scanf("%f%f%f%f%f",&x,&y,&r,&x1,&y1);
    a=(((x1-x)*(x1-x))+((y1-y)*(y1-y)));
    b=r*r;
    c=a-b;
if (c<=0){
    if (c==0){
        printf("Point is on the circle.");
    }
    else {
         printf("Point is inside the circle.");
    }
}
else {
    printf("Point is outside the circle.");
}
    return 0;
}
```

</details>

## Bài 45 · Đề 2812 — Thừa dấu chấm so với oracle chấm bài

`case_f4a64c7407896ece` · AI đề xuất · có căn cứ code/log

NẾU một hoặc nhiều chuỗi printf có dấu chấm cuối câu VÀ log mong đợi cùng nội dung nhưng không có dấu chấm THÌ gợi ý lỗi: Thừa dấu chấm so với oracle chấm bài.

Các nhánh đang phân loại dấu phù hợp với test; sai khác được trích dẫn là dấu chấm. Bài 33 chỉ thêm dấu chấm ở nhánh dương.

**Gợi ý giảng lại:** Kiểm tra lại mẫu output với người ra đề trước khi yêu cầu sửa dấu câu.

**Giới hạn:** Tài liệu rà soát trước đó ghi nhận ví dụ đề 2812 có dấu chấm nhưng oracle không có. Đây là bất nhất cần kiểm chứng, không phải bằng chứng chắc chắn học viên sai kiến thức.

**Dòng căn cứ:** [7, 10, 12]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `-12`; mong đợi `-12.0000 is negative`; thực tế `-12.0000 is negative.`.

Test 2: input `0`; mong đợi `input is zero`; thực tế `input is zero.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main(){
   float a;
   scanf("%f",&a);//input float value a.
   if (a==0)        //Check if a=0.
   { printf("input is zero.");}//display of output.
   
   else { if (a>0) //using another subcondition to check if a>0 or a<0.
          { printf("%.4f is positive.",a);}
          else 
          { printf("%.4f is negative.",a);}
   }
	
	return 0;
}
```

</details>

## Bài 46 · Đề 2825 — So sánh bình phương khoảng cách với bán kính chưa bình phương

`case_f756bf3700e93903` · AI đề xuất · có căn cứ code/log

NẾU code dùng d² nhưng đối chiếu trực tiếp với r VÀ điểm trên đường tròn bán kính 5 bị báo là ở ngoài THÌ gợi ý lỗi: So sánh bình phương khoảng cách với bán kính chưa bình phương.

Hai vế đang khác đại lượng: d² phải so với r², hoặc d so với r. Ở test 3, d² = 25 và r = 5, nên phép so sánh hiện tại làm lệch kết luận.

**Gợi ý giảng lại:** Cho học viên viết rõ d, d², r, r² rồi chọn một cặp nhất quán.

**Giới hạn:** Bài 46 có tính sqrtf(c) vào d nhưng không dùng d để so sánh, đồng thời thiếu math.h. Nhãn này mô tả sai khác công thức thấy trong code/log, không chứng minh niềm tin của người học.

**Dòng căn cứ:** [11, 12, 13, 15]. **Test trượt tham chiếu:** ['3', '4', '5', '6'].

Test 3: input `3.0 4.0 5.0 7.0 7.0`; mong đợi `Point is on the Circle.`; thực tế `Point is outside the Circle.`.

Test 4: input `3.0 4.0 5.0 5.6 6.2`; mong đợi `Point is inside the Circle.`; thực tế `Point is outside the Circle.`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
 float x,y;//cordinate of the center of the circle
 float r;// radius of the circle
 float x1,y1;// the another cordinate provided by user
 scanf("%f%f%f%f%f",&x,&y,&r,&x1,&y1);
 float a=(x1-x)*(x1-x);
 float b=(y1-y)*(y1-y);
 float c=a+b;//distance between origen and cordinates providade by user
 float d=sqrtf(c);
 if(c<r)
 printf("Point is inside the Circle.");
 else if(c==r)
     printf("Point is on the Circle.");
else
    printf("Point is outside the Circle.");
    return 0;
}

```

</details>

## Bài 47 · Đề 2812 — In số hai lần và dùng mẫu định dạng không thống nhất

`case_fa7f4899a2792c11` · AI đề xuất · có căn cứ code/log

NẾU code in số trước if rồi lại in số trong nhánh âm/dương VÀ log có hai giá trị số nối nhau, hoặc thêm số trước thông báo zero THÌ gợi ý lỗi: In số hai lần và dùng mẫu định dạng không thống nhất.

Lệnh in trước chuỗi if luôn chạy. Các nhánh sau lại in giá trị lần nữa bằng %f, nên output vừa lặp số vừa khác số chữ số thập phân.

**Gợi ý giảng lại:** Bỏ lệnh in chung phía trước và để mỗi nhánh tự in đầy đủ một thông báo.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [9, 12, 15, 18]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `-12`; mong đợi `-12.0000 is negative`; thực tế `-12.0000 -12.000000 is negative`.

Test 2: input `0`; mong đợi `input is zero`; thực tế `0.0000input is zero`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main(){
    float n ;         /* variable declaration*/
    
        

            scanf("%f",&n);
        printf("%.4f",n);
     
    if(n<0)
        {printf(" %f is negative",n);}
    
    else if(n>0)
    {printf("%f is positive",n);}
    
    else
    {printf("input is zero");}
    
}
```

</details>

## Bài 48 · Đề 2825 — Thiếu dấu chấm cuối thông báo

`case_fa86ec75d995a3b5` · AI đề xuất · có căn cứ code/log

NẾU chuỗi printf không có dấu chấm cuối câu VÀ output ghi nhận khớp nội dung phân loại nhưng thiếu dấu chấm so với oracle THÌ gợi ý lỗi: Thiếu dấu chấm cuối thông báo.

Khác biệt nhìn thấy trong các test là dấu chấm cuối câu. Không có căn cứ từ sai khác này để kết luận học viên chưa hiểu công thức khoảng cách.

**Gợi ý giảng lại:** Đối chiếu chuỗi output với mẫu, kể cả dấu câu.

**Giới hạn:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

**Dòng căn cứ:** [10, 15, 19]. **Test trượt tham chiếu:** ['1', '2', '3', '4', '5', '6', '7'].

Test 1: input `1.2 2.3 2.7 5.3 7.6`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the Circle`.

Test 2: input `0.0 0.0 5.0 3.0 7.0`; mong đợi `Point is outside the Circle.`; thực tế `Point is outside the Circle`.

<details><summary>Code gốc</summary>

```c
#include<stdio.h>

int main()
{
    float x, y, r, x1, y1;
    scanf ("%f %f %f %f %f",&x,&y,&r,&x1,&y1);
    {
        if ((x1-x)*(x1-x)+(y1-y)*(y1-y)==r*r)
        {
            printf ("Point is on the Circle");
        }
        else
        if ((x1-x)*(x1-x)+(y1-y)*(y1-y)>r*r)
        {
            printf ("Point is outside the Circle");
        }
        else
        {
            printf ("Point is inside the Circle");
        }
    }
    return 0;
}
```

</details>

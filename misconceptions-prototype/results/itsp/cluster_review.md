# ITSP — hồ sơ duyệt cụm

Cụm/luật là biểu hiện lỗi, chưa phải misconception đã được chuyên gia xác nhận.
Báo cáo minh họa dùng agglomerative + cấu trúc, k=3, seed=42 định trước; không chọn theo holdout.
ID sinh viên không có: split chỉ chống trùng source chính xác, chưa bảo đảm độc lập người học.
Đọc kèm data/itsp audit và bản *_correct.c; không dùng bản sửa đúng làm feature.

## Bài 2825

Trạng thái: ok

### Cụm 0 — bài đại diện itsp-2825-271154_buggy

Nguồn: `ITSP@0553f683f99403efb5ef440af826c1d229a52376:dataset/Lab-4/2825/271154_buggy.c`

Bài gốc: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-4/2825/271154_buggy.c`
Bản sửa cùng cặp: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-4/2825/271154_correct.c`
Test nghi lỗi định dạng: `[]`

```json
{
  "test:1": "pass",
  "test:2": "pass",
  "test:3": "fail",
  "test:4": "fail",
  "test:5": "fail",
  "test:6": "fail",
  "test:7": "pass",
  "ast:c_for": "0",
  "ast:c_while": "0",
  "ast:c_do": "0",
  "ast:c_if": "1",
  "ast:c_inclusive_comparison": "0",
  "ast:c_strict_comparison": "1",
  "ast:c_subscript": "0",
  "ast:c_zero_index": "0",
  "ast:c_one_index": "0",
  "ast:c_pointer_declarator": "0",
  "ast:c_pointer_parameter": "0",
  "ast:c_array_parameter": "0",
  "ast:c_address_of": "1",
  "ast:c_dereference": "0",
  "ast:c_update": "0",
  "ast:c_return": "1",
  "ast:parse": "ok"
}
```

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

Nhận xét chuyên gia: CHƯA GÁN NHÃN. Kiểm tra test, định dạng output, runtime và bản sửa trước khi kết luận nguyên nhân.

### Cụm 1 — bài đại diện itsp-2825-271173_buggy

Nguồn: `ITSP@0553f683f99403efb5ef440af826c1d229a52376:dataset/Lab-4/2825/271173_buggy.c`

Bài gốc: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-4/2825/271173_buggy.c`
Bản sửa cùng cặp: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-4/2825/271173_correct.c`
Test nghi lỗi định dạng: `[]`

```json
{
  "test:1": "fail",
  "test:2": "fail",
  "test:3": "pass",
  "test:4": "pass",
  "test:5": "pass",
  "test:6": "pass",
  "test:7": "fail",
  "ast:c_for": "0",
  "ast:c_while": "0",
  "ast:c_do": "0",
  "ast:c_if": "1",
  "ast:c_inclusive_comparison": "0",
  "ast:c_strict_comparison": "1",
  "ast:c_subscript": "0",
  "ast:c_zero_index": "0",
  "ast:c_one_index": "0",
  "ast:c_pointer_declarator": "0",
  "ast:c_pointer_parameter": "0",
  "ast:c_array_parameter": "0",
  "ast:c_address_of": "1",
  "ast:c_dereference": "0",
  "ast:c_update": "0",
  "ast:c_return": "1",
  "ast:parse": "ok"
}
```

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

Nhận xét chuyên gia: CHƯA GÁN NHÃN. Kiểm tra test, định dạng output, runtime và bản sửa trước khi kết luận nguyên nhân.

### Cụm 2 — bài đại diện itsp-2825-271163_buggy

Nguồn: `ITSP@0553f683f99403efb5ef440af826c1d229a52376:dataset/Lab-4/2825/271163_buggy.c`

Bài gốc: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-4/2825/271163_buggy.c`
Bản sửa cùng cặp: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-4/2825/271163_correct.c`
Test nghi lỗi định dạng: `[]`

```json
{
  "test:1": "fail",
  "test:2": "fail",
  "test:3": "fail",
  "test:4": "fail",
  "test:5": "fail",
  "test:6": "fail",
  "test:7": "fail",
  "ast:c_for": "0",
  "ast:c_while": "0",
  "ast:c_do": "0",
  "ast:c_if": "1",
  "ast:c_inclusive_comparison": "0",
  "ast:c_strict_comparison": "1",
  "ast:c_subscript": "0",
  "ast:c_zero_index": "0",
  "ast:c_one_index": "0",
  "ast:c_pointer_declarator": "0",
  "ast:c_pointer_parameter": "0",
  "ast:c_array_parameter": "0",
  "ast:c_address_of": "1",
  "ast:c_dereference": "0",
  "ast:c_update": "0",
  "ast:c_return": "1",
  "ast:parse": "ok"
}
```

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

Nhận xét chuyên gia: CHƯA GÁN NHÃN. Kiểm tra test, định dạng output, runtime và bản sửa trước khi kết luận nguyên nhân.

### Luật mô tả cụm

```json
{
  "target": "cluster_id_only_not_validated_misconception",
  "train_fidelity": 0.9375,
  "holdout_fidelity": 0.8333333333333334,
  "holdout_majority_baseline_fidelity": 0.5,
  "rules": [
    {
      "if": [
        "NOT (test:1=fail)"
      ],
      "then_cluster": 0,
      "train_support": 5,
      "train_precision": 1.0,
      "holdout_support": 2,
      "holdout_precision": 1.0
    },
    {
      "if": [
        "test:1=fail",
        "NOT (test:4=fail)"
      ],
      "then_cluster": 1,
      "train_support": 2,
      "train_precision": 0.5,
      "holdout_support": 2,
      "holdout_precision": 0.5
    },
    {
      "if": [
        "test:1=fail",
        "test:4=fail"
      ],
      "then_cluster": 2,
      "train_support": 9,
      "train_precision": 1.0,
      "holdout_support": 2,
      "holdout_precision": 1.0
    }
  ]
}
```

## Bài 2812

Trạng thái: ok

### Cụm 0 — bài đại diện itsp-2812-270293_buggy

Nguồn: `ITSP@0553f683f99403efb5ef440af826c1d229a52376:dataset/Lab-3/2812/270293_buggy.c`

Bài gốc: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-3/2812/270293_buggy.c`
Bản sửa cùng cặp: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-3/2812/270293_correct.c`
Test nghi lỗi định dạng: `[]`

```json
{
  "test:1": "fail",
  "test:2": "fail",
  "test:3": "fail",
  "test:4": "fail",
  "test:5": "fail",
  "test:6": "fail",
  "test:7": "fail",
  "ast:c_for": "0",
  "ast:c_while": "0",
  "ast:c_do": "0",
  "ast:c_if": "1",
  "ast:c_inclusive_comparison": "0",
  "ast:c_strict_comparison": "1",
  "ast:c_subscript": "0",
  "ast:c_zero_index": "0",
  "ast:c_one_index": "0",
  "ast:c_pointer_declarator": "0",
  "ast:c_pointer_parameter": "0",
  "ast:c_array_parameter": "0",
  "ast:c_address_of": "1",
  "ast:c_dereference": "0",
  "ast:c_update": "0",
  "ast:c_return": "1",
  "ast:parse": "ok"
}
```

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

Nhận xét chuyên gia: CHƯA GÁN NHÃN. Kiểm tra test, định dạng output, runtime và bản sửa trước khi kết luận nguyên nhân.

### Cụm 1 — bài đại diện itsp-2812-270277_buggy

Nguồn: `ITSP@0553f683f99403efb5ef440af826c1d229a52376:dataset/Lab-3/2812/270277_buggy.c`

Bài gốc: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-3/2812/270277_buggy.c`
Bản sửa cùng cặp: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-3/2812/270277_correct.c`
Test nghi lỗi định dạng: `[]`

```json
{
  "test:1": "pass",
  "test:2": "fail",
  "test:3": "pass",
  "test:4": "pass",
  "test:5": "pass",
  "test:6": "pass",
  "test:7": "fail",
  "ast:c_for": "0",
  "ast:c_while": "0",
  "ast:c_do": "0",
  "ast:c_if": "1",
  "ast:c_inclusive_comparison": "0",
  "ast:c_strict_comparison": "1",
  "ast:c_subscript": "0",
  "ast:c_zero_index": "0",
  "ast:c_one_index": "0",
  "ast:c_pointer_declarator": "0",
  "ast:c_pointer_parameter": "0",
  "ast:c_array_parameter": "0",
  "ast:c_address_of": "1",
  "ast:c_dereference": "0",
  "ast:c_update": "0",
  "ast:c_return": "1",
  "ast:parse": "ok"
}
```

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

Nhận xét chuyên gia: CHƯA GÁN NHÃN. Kiểm tra test, định dạng output, runtime và bản sửa trước khi kết luận nguyên nhân.

### Cụm 2 — bài đại diện itsp-2812-270283_buggy

Nguồn: `ITSP@0553f683f99403efb5ef440af826c1d229a52376:dataset/Lab-3/2812/270283_buggy.c`

Bài gốc: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-3/2812/270283_buggy.c`
Bản sửa cùng cặp: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-3/2812/270283_correct.c`
Test nghi lỗi định dạng: `[]`

```json
{
  "test:1": "fail",
  "test:2": "pass",
  "test:3": "fail",
  "test:4": "fail",
  "test:5": "fail",
  "test:6": "fail",
  "test:7": "pass",
  "ast:c_for": "0",
  "ast:c_while": "0",
  "ast:c_do": "0",
  "ast:c_if": "1",
  "ast:c_inclusive_comparison": "0",
  "ast:c_strict_comparison": "1",
  "ast:c_subscript": "0",
  "ast:c_zero_index": "0",
  "ast:c_one_index": "0",
  "ast:c_pointer_declarator": "0",
  "ast:c_pointer_parameter": "0",
  "ast:c_array_parameter": "0",
  "ast:c_address_of": "1",
  "ast:c_dereference": "0",
  "ast:c_update": "0",
  "ast:c_return": "1",
  "ast:parse": "ok"
}
```

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

Nhận xét chuyên gia: CHƯA GÁN NHÃN. Kiểm tra test, định dạng output, runtime và bản sửa trước khi kết luận nguyên nhân.

### Luật mô tả cụm

```json
{
  "target": "cluster_id_only_not_validated_misconception",
  "train_fidelity": 0.9285714285714286,
  "holdout_fidelity": 0.2,
  "holdout_majority_baseline_fidelity": 0.2,
  "rules": [
    {
      "if": [
        "NOT (test:6=fail)"
      ],
      "then_cluster": 1,
      "train_support": 2,
      "train_precision": 1.0,
      "holdout_support": 0,
      "holdout_precision": null
    },
    {
      "if": [
        "test:6=fail",
        "NOT (ast:c_strict_comparison=1)"
      ],
      "then_cluster": 0,
      "train_support": 2,
      "train_precision": 1.0,
      "holdout_support": 0,
      "holdout_precision": null
    },
    {
      "if": [
        "test:6=fail",
        "ast:c_strict_comparison=1"
      ],
      "then_cluster": 0,
      "train_support": 10,
      "train_precision": 0.9,
      "holdout_support": 5,
      "holdout_precision": 0.2
    }
  ]
}
```

## Bài 2833

Trạng thái: ok

### Cụm 0 — bài đại diện itsp-2833-271920_buggy

Nguồn: `ITSP@0553f683f99403efb5ef440af826c1d229a52376:dataset/Lab-4/2833/271920_buggy.c`

Bài gốc: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-4/2833/271920_buggy.c`
Bản sửa cùng cặp: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-4/2833/271920_correct.c`
Test nghi lỗi định dạng: `[]`

```json
{
  "test:1": "fail",
  "test:2": "fail",
  "test:3": "fail",
  "test:4": "fail",
  "test:5": "fail",
  "test:6": "fail",
  "ast:c_for": "1",
  "ast:c_while": "0",
  "ast:c_do": "0",
  "ast:c_if": "1",
  "ast:c_inclusive_comparison": "1",
  "ast:c_strict_comparison": "1",
  "ast:c_subscript": "0",
  "ast:c_zero_index": "0",
  "ast:c_one_index": "0",
  "ast:c_pointer_declarator": "0",
  "ast:c_pointer_parameter": "0",
  "ast:c_array_parameter": "0",
  "ast:c_address_of": "1",
  "ast:c_dereference": "0",
  "ast:c_update": "1",
  "ast:c_return": "1",
  "ast:parse": "ok"
}
```

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

Nhận xét chuyên gia: CHƯA GÁN NHÃN. Kiểm tra test, định dạng output, runtime và bản sửa trước khi kết luận nguyên nhân.

### Cụm 1 — bài đại diện itsp-2833-271986_buggy

Nguồn: `ITSP@0553f683f99403efb5ef440af826c1d229a52376:dataset/Lab-4/2833/271986_buggy.c`

Bài gốc: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-4/2833/271986_buggy.c`
Bản sửa cùng cặp: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-4/2833/271986_correct.c`
Test nghi lỗi định dạng: `[]`

```json
{
  "test:1": "pass",
  "test:2": "pass",
  "test:3": "pass",
  "test:4": "fail",
  "test:5": "fail",
  "test:6": "pass",
  "ast:c_for": "1",
  "ast:c_while": "0",
  "ast:c_do": "0",
  "ast:c_if": "1",
  "ast:c_inclusive_comparison": "1",
  "ast:c_strict_comparison": "1",
  "ast:c_subscript": "0",
  "ast:c_zero_index": "0",
  "ast:c_one_index": "0",
  "ast:c_pointer_declarator": "0",
  "ast:c_pointer_parameter": "0",
  "ast:c_array_parameter": "0",
  "ast:c_address_of": "1",
  "ast:c_dereference": "0",
  "ast:c_update": "1",
  "ast:c_return": "1",
  "ast:parse": "ok"
}
```

```c
#include<stdio.h>

int main()
{
int N,d=0;
float a=1,b=1,c=1,x,y,z;
scanf("%d",&N);
    for(a=1;a<=N;a++){
        for(b=1;b<=a;b++){
            for(c=1;c<=b;c++){
                x=((a*a)+(b*b)-(c*c))/(2*a*b);
y=((a*a)+(c*c)-(b*b))/(2*a*c);
z=((b*b)+(c*c)-(a*a))/(2*b*c);
                if(x<1&&x>-1&&y<1&&y>-1&&z<1&&z>-1&&a>=b&&b>=c&&a>=c)
                    if((x<0&&y>0&&z>0)||(y<0&&x>0&&z>0)||(z<0&&x>0&&y>0)||(x>0&&y>0&&z>0)||(x=0&&y!=0&&z!=0)||(y=0&&x!=0&&z!=0)||(z=0&&x!=0&&y!=0))
                d=d+1;
            }
        }
    }   
    printf("Number of possible triangles is %d",d);
return 0;
}
```

Nhận xét chuyên gia: CHƯA GÁN NHÃN. Kiểm tra test, định dạng output, runtime và bản sửa trước khi kết luận nguyên nhân.

### Cụm 2 — bài đại diện itsp-2833-271965_buggy

Nguồn: `ITSP@0553f683f99403efb5ef440af826c1d229a52376:dataset/Lab-4/2833/271965_buggy.c`

Bài gốc: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-4/2833/271965_buggy.c`
Bản sửa cùng cặp: `E:/AAI/misconceptions-prototype/data/raw/itsp/dataset/Lab-4/2833/271965_correct.c`
Test nghi lỗi định dạng: `[]`

```json
{
  "test:1": "fail",
  "test:2": "pass",
  "test:3": "fail",
  "test:4": "fail",
  "test:5": "fail",
  "test:6": "fail",
  "ast:c_for": "1",
  "ast:c_while": "0",
  "ast:c_do": "0",
  "ast:c_if": "1",
  "ast:c_inclusive_comparison": "1",
  "ast:c_strict_comparison": "1",
  "ast:c_subscript": "0",
  "ast:c_zero_index": "0",
  "ast:c_one_index": "0",
  "ast:c_pointer_declarator": "0",
  "ast:c_pointer_parameter": "0",
  "ast:c_array_parameter": "0",
  "ast:c_address_of": "1",
  "ast:c_dereference": "0",
  "ast:c_update": "0",
  "ast:c_return": "1",
  "ast:parse": "ok"
}
```

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

Nhận xét chuyên gia: CHƯA GÁN NHÃN. Kiểm tra test, định dạng output, runtime và bản sửa trước khi kết luận nguyên nhân.

### Luật mô tả cụm

```json
{
  "target": "cluster_id_only_not_validated_misconception",
  "train_fidelity": 0.9230769230769231,
  "holdout_fidelity": 0.8,
  "holdout_majority_baseline_fidelity": 0.6,
  "rules": [
    {
      "if": [
        "NOT (test:2=pass)"
      ],
      "then_cluster": 0,
      "train_support": 5,
      "train_precision": 1.0,
      "holdout_support": 1,
      "holdout_precision": 1.0
    },
    {
      "if": [
        "test:2=pass",
        "NOT (ast:c_update=1)"
      ],
      "then_cluster": 2,
      "train_support": 5,
      "train_precision": 1.0,
      "holdout_support": 1,
      "holdout_precision": 1.0
    },
    {
      "if": [
        "test:2=pass",
        "ast:c_update=1"
      ],
      "then_cluster": 2,
      "train_support": 3,
      "train_precision": 0.6666666666666666,
      "holdout_support": 3,
      "holdout_precision": 0.6666666666666666
    }
  ]
}
```

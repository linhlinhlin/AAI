# Repair-label audit packet

Judge only whether the category describes what the minimal repair changes in the program. Do not judge the student's beliefs.

## audit-001 · lab04-ex03 · assigned BRANCH_CONDITION

Details: branch_condition:->( num_max -, branch_condition:->)

```diff
--- failing.c
+++ minimal_repair.c
@@ -18,5 +18,6 @@
         for (linha = 0; linha < num_max; linha++) {
                 for (i = 0; i < n; i++) {
-                    if (valores[i] > linha)
+
+                    if ((num_max - valores[i]) > linha)
                         printf(" ");
                     else
```

## audit-002 · lab02-ex02 · assigned BRANCH_CONDITION

Details: branch_condition:>-><

```diff
--- failing.c
+++ minimal_repair.c
@@ -5,5 +5,5 @@
     int a, b;
     scanf("%d%d", &a,&b);
-    if (b>a){
+    if (b<a){
         int temp=a;
         a=b;
```

## audit-003 · lab02-ex03 · assigned BRANCH_CONDITION

Details: branch_condition:->a %, branch_condition:% a->, branch_condition:0 && b !=->

```diff
--- failing.c
+++ minimal_repair.c
@@ -5,5 +5,5 @@
     int a, b;
     scanf("%d %d", &a, &b);
-    if (b % a == 0 && b != 0) printf("yes\n");
+    if (a % b == 0) printf("yes\n");
     else printf("no\n");    
     return 0;
```

## audit-004 · lab04-ex03 · assigned COMPUTATION

Details: computation:4->max

```diff
--- failing.c
+++ minimal_repair.c
@@ -15,5 +15,5 @@
     i = 0;
     while (i < n) {
-        v[i] -= 4;
+        v[i] -= max;
         i++;
     }
```

## audit-005 · lab02-ex02 · assigned COMPUTATION

Details: output_argument:->y ,, output_argument:, y->, output_argument:->x ,, output_argument:, x->

```diff
--- failing.c
+++ minimal_repair.c
@@ -4,6 +4,6 @@
     int x, y;
     scanf("%d%d", &x, &y);
-    if (x>=y) printf("%d\n%d\n",x,y);
-    else printf("%d\n%d\n",y,x);
+    if (x>=y) printf("%d\n%d\n",y,x);
+    else printf("%d\n%d\n",x,y);
     return 0;
 }
```

## audit-006 · lab04-ex04 · assigned COMPUTATION

Details: computation:->- 1

```diff
--- failing.c
+++ minimal_repair.c
@@ -8,5 +8,5 @@
     true=1;
     i=0;
-    x=strlen(vet);
+    x=strlen(vet)-1;
     while (i<x)
     {
```

## audit-007 · lab02-ex03 · assigned CONTROL_FLOW

Details: insert:return_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -14,3 +14,4 @@
     }
     
+    return 0;
 }
```

## audit-008 · lab02-ex01 · assigned CONTROL_FLOW

Details: insert:return_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -9,3 +9,4 @@
     if (c>a)a=c;
     printf("%d\n", a);
+    return 0;
 }
```

## audit-009 · lab04-ex06 · assigned CONTROL_FLOW

Details: insert:return_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -39,3 +39,4 @@
     maiusculas(s);
     printf("%s\n",s);
+    return 0;
 }
```

## audit-010 · lab03-ex02 · assigned EXTRA_STATEMENT

Details: delete:expression_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -19,5 +19,4 @@
             putchar(j < N + i - 1 ? ' ' : '\n');
         }
-        printf("%d\n", j);
     }
 }
```

## audit-011 · lab03-ex04 · assigned EXTRA_STATEMENT

Details: delete:expression_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -12,5 +12,4 @@
             num = num * 10 + c;
             c = getchar();
-            printf("\n%ld\n", num);
         }
         (c == EOF) ? printf("%ld", num) : printf("%ld%c", num, c);
```

## audit-012 · lab03-ex07 · assigned EXTRA_STATEMENT

Details: delete:expression_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -39,6 +39,4 @@
         }
 
-        printf("%d\n", res);
-
         oper = getchar();
     }
```

## audit-013 · lab02-ex06 · assigned INPUT

Details: input:"%d"->"%f"

```diff
--- failing.c
+++ minimal_repair.c
@@ -11,5 +11,5 @@
     while (n>1){
         n--;
-        scanf("%d", &f);
+        scanf("%f", &f);
         if (f > max)
             max = f;
```

## audit-014 · lab03-ex07 · assigned LOOP_BOUNDARY

Details: loop_header:'1'->'0'

```diff
--- failing.c
+++ minimal_repair.c
@@ -20,5 +20,5 @@
         g = i;
 
-        while (s[g] >='1' && s[g] <='9' && (s[g+1] != ' ' || s[g+1] != '\0'))
+        while (s[g] >='0' && s[g] <='9' && (s[g+1] != ' ' || s[g+1] != '\0'))
         {    
             num = (int)(s[g]);
```

## audit-015 · lab03-ex06 · assigned LOOP_BOUNDARY

Details: loop_header:<=-><

```diff
--- failing.c
+++ minimal_repair.c
@@ -14,5 +14,5 @@
     num[i] = '\0';
 
-    for(j = 0; j <= i; j++){
+    for(j = 0; j < i; j++){
         sum += (num[j] - '0');
     }
```

## audit-016 · lab03-ex06 · assigned LOOP_BOUNDARY

Details: loop_header:'\n'->EOF

```diff
--- failing.c
+++ minimal_repair.c
@@ -6,5 +6,5 @@
 
 int main () {
-    while ((c = getchar()) != '\n') {
+    while ((c = getchar()) != EOF) {
         if (c >= 48 && c <= 57)
             soma_alg += c - 48;
```

## audit-017 · lab02-ex04 · assigned MISSING_STATEMENT

Details: insert:expression_statement+return_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -54,4 +54,6 @@
 
     }
+    printf("%ld %ld %ld\n", menor, meio, maior);
+    return 0;
     
 }
```

## audit-018 · lab04-ex07 · assigned MISSING_STATEMENT

Details: insert:expression_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -13,4 +13,5 @@
 	s[j] = s[j+1];
       s[j] = '0';
+      --i;
     }
```

## audit-019 · lab02-ex10 · assigned MISSING_STATEMENT

Details: insert:expression_statement+while_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -6,4 +6,20 @@
 
 int main(){
+    int N, num_digits = 0, sum = 0, temp = 0;
+    scanf("%d", &N);
+    temp = N;
+    while (temp != 0){
+        num_digits++;
+        temp /= 10;
+    }
+    temp = N;
+
+    while (temp != 0){
+        sum += temp % 10;
+        temp /= 10;
+    }
+    printf("%d\n", num_digits);
+    printf("%d\n", sum);
+
     return 0;
 }
```

## audit-020 · lab02-ex02 · assigned MULTI

Details: branch_condition:>-><, insert:return_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -6,7 +6,8 @@
     int n, m;
     scanf("%d%d", &n, &m);
-    if (n > m)
+    if (n < m)
         printf("%d\n%d\n", n, m);
     else 
         printf("%d\n%d\n", m, n);
+    return 0;
 }
```

## audit-021 · lab03-ex04 · assigned MULTI

Details: moved:}, other:imprimir->vistoNaoZero, branch_condition:&&->||, insert:output_literal_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -8,10 +8,14 @@
     int c;
     int estado = FORA;
-    int imprimir = 0;
+    int vistoNaoZero = 0;
 
-    while((c = getchar()) != EOF) {
-        if (c == ' ' && c == '\n') {
+    while ((c = getchar()) != EOF) {
+
+        if (c == ' ' || c == '\n') {
+            if (estado == DENTRO && !vistoNaoZero)
+                putchar('0');
+
             estado = FORA;
-            imprimir = 0;
+            vistoNaoZero = 0;
             putchar(c);
         }
@@ -19,25 +23,20 @@
             if (estado == FORA) {
                 estado = DENTRO;
+                vistoNaoZero = 0;
+            }
+
                 if (c != '0') {
-                    imprimir = 1;
+                vistoNaoZero = 1;
                     putchar(c);
                 }
-                else {
-                    imprimir = 0;
-                }
-            }
-            else {
-                if (c != '0' || imprimir) {
+            else if (vistoNaoZero) {
                     putchar(c);
-                    imprimir = 1;
-                }
-            }
-            if (estado == DENTRO && c == '0' && !imprimir) {
-                putchar(c);
-                imprimir = 1;
             }
         }
     }
 
+    if (estado == DENTRO && !vistoNaoZero)
+        putchar('0');
+
     return 0;
 }
```

## audit-022 · lab02-ex02 · assigned MULTI

Details: output_argument:->menor ,, output_argument:, menor->, insert:return_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -12,4 +12,5 @@
         menor = a;
     }
-    printf("%d\n%d\n", maior, menor);
+    printf("%d\n%d\n", menor, maior);
+    return 0;
 }
```

## audit-023 · lab02-ex09 · assigned OUTPUT_FORMAT

Details: output_format:"%d:%d:%d\n"->"%02d:%02d:%02d\n"

```diff
--- failing.c
+++ minimal_repair.c
@@ -8,5 +8,5 @@
     m = n / 60;
     s = n % 60;
-    printf("%d:%d:%d\n", h,m,s);
+    printf("%02d:%02d:%02d\n", h,m,s);
     return 0;
 }
```

## audit-024 · lab02-ex08 · assigned OUTPUT_FORMAT

Details: output_format:"%2.f\n"->"%.2f\n"

```diff
--- failing.c
+++ minimal_repair.c
@@ -16,5 +16,5 @@
 
     media = soma / N;
-    printf("%2.f\n", media);
+    printf("%.2f\n", media);
 
     return 0;
```

## audit-025 · lab02-ex09 · assigned OUTPUT_FORMAT

Details: output_format:"%d:%d:%d\n"->"%02d:%02d:%02d\n"

```diff
--- failing.c
+++ minimal_repair.c
@@ -7,5 +7,5 @@
 	minutos=n/60 - horas*60;
 	segundos=n%60;
-	printf("%d:%d:%d\n",horas,minutos,segundos);
+	printf("%02d:%02d:%02d\n",horas,minutos,segundos);
 	return 0;
 }
```

## audit-026 · lab03-ex02 · assigned OUTPUT_TEXT

Details: output_text:"%d "->"%d", insert:output_literal_statement, output_text:"%d "->" %d"

```diff
--- failing.c
+++ minimal_repair.c
@@ -9,9 +9,10 @@
 
             for(j = 1; j <= i; j++){
-                printf("%d ", j);
+                printf("%d", j);
+                if (j < i) printf(" ");
             }
 
             for(j = i-1; j >= 1; j--){
-                printf("%d ", j);
+                printf(" %d", j);
             }
```

## audit-027 · lab03-ex03 · assigned OUTPUT_TEXT

Details: insert:output_literal_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -17,4 +17,7 @@
 			else
 				printf("-");
+
+			if(col_n != N)
+				printf(" ");
 		}
```

## audit-028 · lab03-ex01 · assigned OUTPUT_TEXT

Details: output_text:"       %d"->"\t%d"

```diff
--- failing.c
+++ minimal_repair.c
@@ -18,5 +18,5 @@
         while (count_linhas < n)
         {
-            printf("       %d", count_linhas + v_inicial);
+            printf("\t%d", count_linhas + v_inicial);
             count_linhas++;
         }
```

## audit-029 · lab04-ex02 · assigned STATEMENT_PLACEMENT

Details: declaration_scaffolding, insert:brace

```diff
--- failing.c
+++ minimal_repair.c
@@ -6,13 +6,13 @@
 
 int main (){
-    int n, i, c, l, max = 0;
+    int vec[VECMAX], n, i, c, l, max = 0;
     scanf("%d", &n);
     while (n >= VECMAX || n <= 0)
         scanf("%d\n", &n);
-    int vec[n];
-    for (i = 0; i < n; i++)
+    for (i = 0; i < n; i++){
         scanf("%d", &vec[i]);
         if (vec[i] > max)
             max = vec[i];    
+    }    
     for (l = 0; l < max ; l++){
         for (c = 0; c < n; c++){
```


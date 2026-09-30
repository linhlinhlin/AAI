# Repair-label audit packet

Judge only whether the category describes what the minimal repair changes in the program. Do not judge the student's beliefs.

## audit-001 · lab04-ex02 · assigned BRANCH_CONDITION

Details: branch_condition:<=->>=

```diff
--- failing.c
+++ minimal_repair.c
@@ -33,5 +33,5 @@
         for(j=0;j<n;j++)
         {
-            putchar(vec[j]<=i?'*':' ');
+            putchar(vec[j]>=i?'*':' ');
         }
         putchar('\n');
```

## audit-002 · lab03-ex02 · assigned BRANCH_CONDITION

Details: branch_condition:->> 1

```diff
--- failing.c
+++ minimal_repair.c
@@ -8,5 +8,5 @@
     for (i = 1; i <= n; i++) {
         for (j = 1; j <= n; j++) {
-            if (j)
+            if (j > 1)
                 putchar(' ');
             if (i + j - n > 0)
```

## audit-003 · lab02-ex03 · assigned BRANCH_CONDITION

Details: branch_condition:/->%

```diff
--- failing.c
+++ minimal_repair.c
@@ -8,5 +8,5 @@
 
     scanf("%d%d", &N, &M);
-    if (N/M == 0)
+    if (N%M == 0)
     {
         printf("yes\n");
```

## audit-004 · lab03-ex03 · assigned BRANCH_CONDITION

Details: branch_condition:(->j == n -, branch_condition:% 2 == 0 && j % 2 == 0->- 1, branch_condition:)->

```diff
--- failing.c
+++ minimal_repair.c
@@ -11,5 +11,5 @@
         for (j=0; j<n;j++)
         {
-            if (j==i || (i%2==0 && j%2==0))
+            if (j==i || j==n-i-1)
                 tab[i][j] = '*';
             else
```

## audit-005 · lab02-ex01 · assigned BRANCH_CONDITION

Details: branch_condition:->else

```diff
--- failing.c
+++ minimal_repair.c
@@ -11,5 +11,5 @@
         printf("%d\n", num1);
     }
-    if ((num2 > num1) & (num2 > num3)){
+    else if ((num2 > num1) & (num2 > num3)){
         printf("%d\n", num2);
     }
```

## audit-006 · lab03-ex02 · assigned COMPUTATION

Details: computation:+ 1->

```diff
--- failing.c
+++ minimal_repair.c
@@ -25,5 +25,5 @@
 		num_max = linha;
 		passo = AUMENTA;
-		num_espacos = (n-linha+1)*2;
+		num_espacos = (n-linha)*2;
 		
 		for (espacos = 0; espacos < num_espacos; espacos++)
```

## audit-007 · lab02-ex10 · assigned COMPUTATION

Details: computation:/->%

```diff
--- failing.c
+++ minimal_repair.c
@@ -7,5 +7,5 @@
     scanf("%d", &n);
     while(n>0) {
-        soma = soma + n/AUXILIAR;
+        soma = soma + n%AUXILIAR;
         ++i;
         n = n/AUXILIAR;
```

## audit-008 · lab04-ex07 · assigned COMPUTATION

Details: computation:i->j

```diff
--- failing.c
+++ minimal_repair.c
@@ -26,5 +26,5 @@
         i++;
     }
-    vector[i] = '\0';
+    vector[j] = '\0';
     printf("%s\n", vector);
 }
```

## audit-009 · lab02-ex02 · assigned COMPUTATION

Details: output_argument:&->

```diff
--- failing.c
+++ minimal_repair.c
@@ -6,5 +6,5 @@
     int M;
     scanf("%d %d\n", &N, &M);
-    (N<M) ? printf("%d\n%d\n", &N, &M) : printf("%d\n%d\n" , &M, &N);
+    (N<M) ? printf("%d\n%d\n", N, M) : printf("%d\n%d\n" , M, N);
 
     return 0;
```

## audit-010 · lab03-ex06 · assigned COMPUTATION

Details: computation:atoi ( &->, computation:)->- '0'

```diff
--- failing.c
+++ minimal_repair.c
@@ -7,5 +7,5 @@
     int sum = 0;
     while((c = getchar()) != '\n' && c != EOF){
-        sum += atoi(&c);
+        sum += c - '0';
     }
```

## audit-011 · lab03-ex05 · assigned CONTROL_FLOW

Details: insert:continue_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -7,5 +7,6 @@
 		if (c == '"' && write == 1 && bar == 0){
 			write = 0;
-			putchar('\n');}
+			putchar('\n');
+			continue;}
 		if (c == '"' && write == 0){
 			write = 1;
```

## audit-012 · lab02-ex05 · assigned CONTROL_FLOW

Details: insert:return_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -8,3 +8,4 @@
     for (i = 1; i <= n; i++)
         printf("%d\n", i);
+    return 0;
 }
```

## audit-013 · lab02-ex06 · assigned CONTROL_FLOW

Details: insert:return_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -19,3 +19,4 @@
     }
     printf("min: %f, max: %f\n", min, max);
+    return 0;
 }
```

## audit-014 · lab02-ex05 · assigned CONTROL_FLOW

Details: insert:return_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -10,3 +10,4 @@
         printf("%d\n", contador);
     }
+    return 0;
 }
```

## audit-015 · lab04-ex04 · assigned CONTROL_FLOW

Details: insert:return_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -26,3 +26,4 @@
         printf("no\n");
     }
+    return 0;
 }
```

## audit-016 · lab02-ex07 · assigned EXTRA_STATEMENT

Details: delete:expression_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -10,8 +10,5 @@
     contador2 = 0;
         while (contador--) {
-            printf("%d asj\n", contador);
             if (contador != 0 && n % contador == 0) {
-                printf("%d a\n", contador);
-                printf("%d\n o", contador2);
                 contador2 ++;
         }
```

## audit-017 · lab04-ex04 · assigned EXTRA_STATEMENT

Details: delete:expression_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -24,5 +24,4 @@
     }
     while (indicador1-cont >= 0){
-        printf("%d/%d-------%d------\n",indicador1,indicador2,cont);
         if (s[indicador1-cont] != s[indicador2+cont]){
             p = NAO;
```

## audit-018 · lab04-ex05 · assigned EXTRA_STATEMENT

Details: delete:expression_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -19,5 +19,4 @@
     s[i] = '\0';
     printf("%s\n", s);
-    printf("%d\n", leLinha(s));
     return 0;
 }
```

## audit-019 · lab02-ex09 · assigned EXTRA_STATEMENT

Details: delete:expression_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -14,5 +14,4 @@
     hh = n / 3600;
     remainder = n % 3600;
-    remainder = n;
     mm = remainder / 60;
     remainder %= 60;
```

## audit-020 · lab04-ex03 · assigned EXTRA_STATEMENT

Details: delete:expression_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -17,6 +17,4 @@
             max_val = numeros[i];
     }
-    
-    printf("%d\n", max_val);
 
     for (linha = 0; linha < max_val; linha++) {
```

## audit-021 · lab02-ex07 · assigned INITIALIZATION

Details: initializer:0->1

```diff
--- failing.c
+++ minimal_repair.c
@@ -5,6 +5,6 @@
     int n, contador, total;
     
-    contador = 0;
-    total = 0;
+    contador = 1;
+    total = 1;
 
     scanf("%d", &n);
```

## audit-022 · lab02-ex02 · assigned INPUT

Details: input:"%d,%d"->"%d%d"

```diff
--- failing.c
+++ minimal_repair.c
@@ -6,5 +6,5 @@
   int n, m;
 
-  scanf("%d,%d", &n, &m);
+  scanf("%d%d", &n, &m);
   if (n < m)
     printf("%d\n%d\n", n, m);
```

## audit-023 · lab02-ex01 · assigned INPUT

Details: declaration_scaffolding, input:"%d,%d,%d"->"%d %d %d"

```diff
--- failing.c
+++ minimal_repair.c
@@ -3,7 +3,7 @@
 
 int main(){
-    int n1,n2,n3;
-    scanf("%d,%d,%d",&n1,&n2,&n3);
-    int maior=n1;
+    int n1,n2,n3,maior;
+    scanf("%d %d %d",&n1,&n2,&n3);
+    maior=n1;
     if (n2>maior){
         maior=n2;
```

## audit-024 · lab02-ex06 · assigned INPUT

Details: input:"%d"->"%f"

```diff
--- failing.c
+++ minimal_repair.c
@@ -7,5 +7,5 @@
   float N, temp, min = FLT_MAX, max = -FLT_MAX;
 
-  scanf("%d", &N);
+  scanf("%f", &N);
 
   for(i = 0; i < N; i++) {
```

## audit-025 · lab02-ex08 · assigned INPUT

Details: input:->&

```diff
--- failing.c
+++ minimal_repair.c
@@ -10,5 +10,5 @@
     scanf("%d", &n);
     while (cont < n){
-        scanf("%f", numero);
+        scanf("%f", &numero);
         soma += numero;
         ++cont;
```

## audit-026 · lab02-ex06 · assigned INPUT

Details: input:->&

```diff
--- failing.c
+++ minimal_repair.c
@@ -9,5 +9,5 @@
     for (i=0; i<num; i++)
     {
-        scanf("%f", dado);
+        scanf("%f", &dado);
         if (i==0)
         {
```

## audit-027 · lab02-ex05 · assigned LOOP_BOUNDARY

Details: loop_header:0->1

```diff
--- failing.c
+++ minimal_repair.c
@@ -9,5 +9,5 @@
     scanf("%d", &N);
 
-    for(i=0; i<=N; ++i) {
+    for(i=1; i<=N; ++i) {
         printf("%d\n",i);
     }
```

## audit-028 · lab03-ex05 · assigned LOOP_BOUNDARY

Details: loop_header:'\n'->EOF

```diff
--- failing.c
+++ minimal_repair.c
@@ -12,5 +12,5 @@
     int simbolo = NOESCAPE;
 
-    while ((c = getchar()) != '\n'){
+    while ((c = getchar()) != EOF){
         if ((c == '"' && estado == FORA))
             estado = DENTRO;
```

## audit-029 · lab03-ex06 · assigned LOOP_BOUNDARY

Details: loop_header:'\n'->EOF

```diff
--- failing.c
+++ minimal_repair.c
@@ -5,5 +5,5 @@
     int c, soma = 0; 
 
-    while((c= getchar()) != '\n')
+    while((c= getchar()) != EOF)
         soma = soma + (c - '0');
     if (soma % 9 == 0)
```

## audit-030 · lab02-ex10 · assigned LOOP_BOUNDARY

Details: loop_header:<->>

```diff
--- failing.c
+++ minimal_repair.c
@@ -7,5 +7,5 @@
 
     scanf("%d", &num);
-    while (num < 0) {
+    while (num > 0) {
         digito = num % 10;
         num_digitos = num_digitos + 1;
```

## audit-031 · lab04-ex05 · assigned LOOP_BOUNDARY

Details: loop_header:->&& c, loop_header:->&& c != EOF

```diff
--- failing.c
+++ minimal_repair.c
@@ -7,5 +7,5 @@
     int i = 0, c;
 
-    for (i = 0; (c = getchar()) != '\n' && i < MAX - 1; i++) {
+    for (i = 0; (c = getchar()) && c != '\n' && c != EOF && i < MAX - 1; i++) {
         s[i] = c;
     }
```

## audit-032 · lab02-ex01 · assigned MISSING_STATEMENT

Details: insert:if_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -8,4 +8,12 @@
     scanf("%d %d %d", &n_1, &n_2, &n_3);
 
+    if (n_1>n_2 && n_1>n_3) {
+        printf("%d\n", n_1);
+    } else if (n_2>n_1 && n_2>n_3) {
+        printf("%d\n", n_2);
+    } else {
+        printf("%d\n", n_3);
+    }
+
     return 0;
 }
```

## audit-033 · lab02-ex06 · assigned MISSING_STATEMENT

Details: insert:expression_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -8,5 +8,7 @@
 
     scanf("%d", &N);
-
+    scanf("%f", &min);
+    max = min;
+    N--;
     while(N--) {
         scanf("%f", &aux);
```

## audit-034 · lab02-ex03 · assigned MISSING_STATEMENT

Details: insert:expression_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -7,4 +7,6 @@
     int N, M;
 
+    scanf("%d%d", &N, &M);
+
     N % M == 0 ? printf("yes\n") : printf("no\n");
```

## audit-035 · lab02-ex03 · assigned MISSING_STATEMENT

Details: insert:expression_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -5,4 +5,6 @@
 {
     int num1, num2;
+
+    scanf("%d%d", &num1, &num2);
 
     if (num1 % num2 == 0)
```

## audit-036 · lab02-ex06 · assigned MISSING_STATEMENT

Details: insert:expression_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -23,4 +23,5 @@
         counter++;
     }
+    printf("min: %f, max: %f\n", min, max);
     return 0;
 }
```

## audit-037 · lab02-ex01 · assigned MULTI

Details: other:maior = 0->max, initializer:maior = 0->max, other:if ( um >= dois && um >= tres ) maior->max, branch_condition:if ( um >= dois && um >= tres ) maior->max

```diff
--- failing.c
+++ minimal_repair.c
@@ -4,13 +4,10 @@
 int main()
 {
-    int um, dois, tres, maior = 0;
+    int um, dois, tres, max;
+
     scanf("%d %d %d", &um, &dois, &tres);
-    if(um >= dois && um >= tres)
-        maior = um;
-    else if(dois >= um && dois >= tres)
-        maior = dois;
-    else
-        maior = tres;
-    printf("%d", maior);
+    max = um > dois ? um : dois;
+    max = max > tres ? max : tres;
+    printf("%d\n", max);
     return 0;
 }
```

## audit-038 · lab03-ex06 · assigned MULTI

Details: declaration_scaffolding, input:scanf ( "%d" , & num )->char c, numeric_type:scanf ( "%d" , & num )->char c, other:scanf ( "%d" , & num )->char c

```diff
--- failing.c
+++ minimal_repair.c
@@ -4,11 +4,10 @@
 
 int main() {
-    int num, digito, soma = 0;
-    scanf("%d", &num);
+    int soma = 0;
+    char c;
 
-    while (num != 0) {
-        digito = num % 10;
-        soma = soma + digito;
-        num = num / 10;
+    
+    while ((c = getchar()) != '\n' && c != ' ' && c != EOF) {
+        soma += c - '0';  
     }
```

## audit-039 · lab04-ex07 · assigned MULTI

Details: moved:void apagaCaracter(char s[], char n){, numeric_type:->void leLinha ( char s [ ] ) {, other:->void leLinha ( char s [ ] ) {, structure

```diff
--- failing.c
+++ minimal_repair.c
@@ -4,14 +4,29 @@
 
 
-void apagaCaracter(char s[], char n){
+
+void leLinha(char s[]){
     int c, contador = 0;
 
     while((c = getchar()) != EOF && c != '\n'){
-        if(c != n)
             s[contador++] = c;
     }
     s[contador] = '\0';
+}
 
-    return contador;
+
+void apagaCaracter(char s[], char n){
+    int i = 0, contador = 0;
+
+    while(s[i + contador] != '\0'){
+        if(s[i + contador] == n){
+            contador++;
+            s[i] = s[i + contador];
+        }
+        else{
+            s[i] = s[i + contador];
+            i++;
+        }
+    }
+    s[i] = '\0';
 }
 
@@ -19,4 +34,5 @@
     char n, str[MAX];
 
+    leLinha(str);
     scanf("%c", &n);
     apagaCaracter(str, n);
```

## audit-040 · lab03-ex05 · assigned MULTI

Details: moved:putchar(c);, branch_condition:->&& ! vem_especial, branch_condition:&& vem_especial != 0->, other:->if ( ! vem_especial )

```diff
--- failing.c
+++ minimal_repair.c
@@ -8,5 +8,5 @@
 
     while ((c = getchar()) != EOF && c != '\n'){
-        if (c == '\"'){
+        if (c == '\"' && !vem_especial){
             if (comecou == 0){
                 comecou = 1;
@@ -16,11 +16,16 @@
             }
         } else if (comecou) {
-            if (c == '\\' && vem_especial != 0){
+            if (c == '\\'){
+                if (!vem_especial)
                 vem_especial = 1;
-            } else if (vem_especial){
+                else{
+                    putchar(c);
+                    vem_especial = 0;                }
+            } else {
+                if (vem_especial)
                 vem_especial = 0;
                 putchar(c);
-            } else if (('a' <= c && c <= 'z') || ('A' <= c && c <= 'Z') || ('0' <= c && c <= '9') || ' ' == c){
-                putchar(c);
+                
+                
             };
         };
```

## audit-041 · lab04-ex05 · assigned MULTI

Details: other:->#define MAX 80 int leLinha ( char s [ ] , numeric_type:->#define MAX 80 int leLinha ( char s [ ] , structure, computation:->#define MAX 80 int leLinha ( char s [ ] 

```diff
--- failing.c
+++ minimal_repair.c
@@ -2,5 +2,32 @@
 #include <stdio.h>
 
+#define MAX 80
+
+int leLinha(char s[]) {
+    int i;
+    char c;
+
+    i = 0;  
+    while (i < MAX - 1 && (c = getchar()) != '\n' && c != EOF) {
+        s[i] = c;
+        i++;
+    }
+
+    s[i] = '\0';
+    
+    return i;
+}
+
 int main() {
+    char s[MAX];
+    int tamanho;
+    int i;
+
+    tamanho = leLinha(s);
+
+    for (i = 0; i < tamanho; i++) {
+        printf("%c", s[i]);
+    }
+    printf("\n");
 
     return 0;
```

## audit-042 · lab02-ex07 · assigned NO_CHANGE

Details: declaration_scaffolding

```diff
--- failing.c
+++ minimal_repair.c
@@ -5,5 +5,5 @@
 int main() {
     
-    int n, num, div;
+    int n, num, div = 0;
 
     scanf("%d", &n);
```

## audit-043 · lab04-ex08 · assigned NO_CHANGE

Details: declaration_scaffolding

```diff
--- failing.c
+++ minimal_repair.c
@@ -8,6 +8,5 @@
 int main(){
     char s1[MAX], s2[MAX];
-    long n1 = 0, n2 = 0;
-    int soma;
+    long soma, n1 = 0, n2 = 0;
 
     scanf("%s%s", s1, s2);
```

## audit-044 · lab04-ex08 · assigned NO_CHANGE

Details: declaration_scaffolding

```diff
--- failing.c
+++ minimal_repair.c
@@ -8,5 +8,5 @@
     long long num1, num2;
     char s1[MAX], s2[MAX];
-    int i;
+    int i = 0;
     scanf("%s%s", s1 ,s2);
```

## audit-045 · lab02-ex02 · assigned NO_CHANGE

Details: declaration_scaffolding

```diff
--- failing.c
+++ minimal_repair.c
@@ -4,5 +4,5 @@
 int main()
 {
-    int n, i, maior, menor;
+    int n, i, maior = 0, menor = 100000;
     for(i = 0; i < 2; i++){
         scanf("%d", &n);
```

## audit-046 · lab02-ex08 · assigned NUMERIC_TYPE

Details: numeric_type:,->; float, numeric_type:; float->,

```diff
--- failing.c
+++ minimal_repair.c
@@ -3,6 +3,6 @@
 int main()
 {
-    int i, s = 0;
-    float N, x, media;
+    int i;
+    float s = 0, N, x, media;
 
     scanf("%f", &N);
```

## audit-047 · lab03-ex06 · assigned NUMERIC_TYPE

Details: numeric_type:int->long, declaration_scaffolding

```diff
--- failing.c
+++ minimal_repair.c
@@ -3,5 +3,6 @@
 #include <stdio.h>
 
-void is_divisivel_por_9(int n);
+void is_divisivel_por_9(long n);
+long soma_digitos(long n);
 
 int main() {
@@ -14,5 +15,5 @@
 }
 
-void is_divisivel_por_9(int n) {
+void is_divisivel_por_9(long n) {
     if (n % 9)
         printf("no\n");
```

## audit-048 · lab04-ex07 · assigned OTHER

Details: other:if->while

```diff
--- failing.c
+++ minimal_repair.c
@@ -32,5 +32,5 @@
     for (i = 0; i < VECMAX; i++)
     {
-        if (s[i + delta] == c)
+        while (s[i + delta] == c)
         {
             delta++;
```

## audit-049 · lab02-ex09 · assigned OTHER

Details: other:360->3600

```diff
--- failing.c
+++ minimal_repair.c
@@ -2,5 +2,5 @@
 #include <stdio.h>
 #define SEG 60
-#define HOURS 360
+#define HOURS 3600
 
 int main(){
```

## audit-050 · lab02-ex09 · assigned OUTPUT_FORMAT

Details: output_format:"0%d:0%d:0%d\n"->"%02d:%02d:%02d\n"

```diff
--- failing.c
+++ minimal_repair.c
@@ -11,5 +11,5 @@
     segundos-=minutos*60;
     
-    printf("0%d:0%d:0%d\n",horas,minutos,segundos);
+    printf("%02d:%02d:%02d\n",horas,minutos,segundos);
     return 0;
 }
```

## audit-051 · lab02-ex09 · assigned OUTPUT_FORMAT

Details: output_format:"%d:%d:%d"->"%.2d:%.2d:%.2d\n"

```diff
--- failing.c
+++ minimal_repair.c
@@ -9,5 +9,5 @@
     minutos = resto / 60;
     segundos = resto % 60;
-    printf("%d:%d:%d", horas, minutos, segundos);
+    printf("%.2d:%.2d:%.2d\n", horas, minutos, segundos);
     return 0;
 }
```

## audit-052 · lab02-ex03 · assigned OUTPUT_FORMAT

Details: output_format:"%d\n"->"yes\n", output_format:"%d\n"->"no\n"

```diff
--- failing.c
+++ minimal_repair.c
@@ -12,7 +12,7 @@
     }
     if (maior%menor==0){ 
-        printf("%d\n", "yes");
+        printf("yes\n");
     } else {
-        printf("%d\n", "no");
+        printf("no\n");
     }
     return 0;
```

## audit-053 · lab02-ex09 · assigned OUTPUT_FORMAT

Details: output_format:"%2d:%2d:%2d\n"->"%02d:%02d:%02d\n"

```diff
--- failing.c
+++ minimal_repair.c
@@ -14,5 +14,5 @@
     m = ((sintro%HORASEMSEG)/MINEMSEG);
     s = (sintro%MINEMSEG);
-printf("%2d:%2d:%2d\n", h, m, s);
+printf("%02d:%02d:%02d\n", h, m, s);
 return 0;
 }
```

## audit-054 · lab02-ex09 · assigned OUTPUT_FORMAT

Details: output_format:"%02x:%02x:%02x\n"->"%02d:%02d:%02d\n"

```diff
--- failing.c
+++ minimal_repair.c
@@ -19,5 +19,5 @@
             HH = MM / 60;
             MM = MM % 60;
-            printf("%02x:%02x:%02x\n",HH,MM,SS);
+            printf("%02d:%02d:%02d\n",HH,MM,SS);
         }
```

## audit-055 · lab03-ex03 · assigned OUTPUT_TEXT

Details: insert:output_literal_statement, output_text:"* "->"*", output_text:"- "->"-"

```diff
--- failing.c
+++ minimal_repair.c
@@ -18,10 +18,12 @@
     for(i = 1; i <= N;i++){
         for(j = 1; j <= N;j++){
-            
+            if(j != 1){
+                printf(" ");
+            }
             if(j == i || j == count){ 
-                printf("* ");
+                printf("*");
             }
             else{
-                printf("- ");
+                printf("-");
             }
```

## audit-056 · lab04-ex05 · assigned OUTPUT_TEXT

Details: insert:output_literal_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -20,4 +20,5 @@
     chara_tuah = getchar();
     }
+    printf("\n");
     return 0;
 }
```

## audit-057 · lab03-ex02 · assigned OUTPUT_TEXT

Details: insert:output_literal_statement

```diff
--- failing.c
+++ minimal_repair.c
@@ -16,4 +16,6 @@
                 printf(" ");
             }
+            if (col < (N + linha - 1))
+                printf(" ");
         }
         printf("\n");
```

## audit-058 · lab02-ex03 · assigned OUTPUT_TEXT

Details: output_text:"yes"->"yes\n", output_text:"no"->"no\n"

```diff
--- failing.c
+++ minimal_repair.c
@@ -7,8 +7,8 @@
 	
 	if (N%M == 0) {
-		printf("yes");
+		printf("yes\n");
 	}
 	else {
-		printf("no");
+		printf("no\n");
 	}
 	return 0;
```

## audit-059 · lab03-ex07 · assigned OUTPUT_TEXT

Details: output_text:"%d"->"%d\n"

```diff
--- failing.c
+++ minimal_repair.c
@@ -36,5 +36,5 @@
         op_total -= numero;
 
-    printf("%d", op_total);
+    printf("%d\n", op_total);
 
     return 0;
```

## audit-060 · lab03-ex03 · assigned STATEMENT_PLACEMENT

Details: moved:putchar('\n');, insert:brace

```diff
--- failing.c
+++ minimal_repair.c
@@ -11,5 +11,4 @@
     scanf("%d", &N);
     cruz(N);
-    putchar('\n');
 
     return 0;
@@ -21,4 +20,5 @@
 
     for(i=0; i<N; i++)
+    {
         for(j=0; j<N; j++)
         {
@@ -27,3 +27,4 @@
             putchar((i == j) || (i+j == N-1) ? '*':'-');
         }
-}+        putchar('\n');
+}}
```

## audit-061 · lab03-ex03 · assigned STATEMENT_PLACEMENT

Details: insert:brace

```diff
--- failing.c
+++ minimal_repair.c
@@ -5,8 +5,9 @@
     int lin, col;
     for (lin = 1; lin <= N; lin++){
-        for (col = 1; col <= N; col++)
+        for (col = 1; col <= N; col++){
             printf("%s", ((col == lin) || ((col + lin) == (N + 1))) ? "*" : "-");
             if (col <  N)
                 putchar(' ');
+        }
         printf("\n");
     }
```

## audit-062 · lab04-ex04 · assigned STATEMENT_PLACEMENT

Details: moved:}

```diff
--- failing.c
+++ minimal_repair.c
@@ -10,7 +10,6 @@
         if(str[i] != str[j])
             return 0;
-
+    }
         return 1;
-    }
 }
```

## audit-063 · lab02-ex06 · assigned STATEMENT_PLACEMENT

Details: moved:}

```diff
--- failing.c
+++ minimal_repair.c
@@ -15,5 +15,4 @@
    {
     scanf("%f", &reaisintrod);
-   }
     if (reaisintrod <= min)
     {
@@ -24,4 +23,5 @@
         max = reaisintrod;
     }
+   }
    printf("min: %f, max: %f\n", min, max);
    return 0;
```

## audit-064 · lab04-ex04 · assigned STATEMENT_PLACEMENT

Details: moved:}

```diff
--- failing.c
+++ minimal_repair.c
@@ -9,8 +9,7 @@
         if (s[i] != s[j])
             return 0;
+    }
         return 1;
     }
-}
-
 int main(){
     char s[MAX];
```


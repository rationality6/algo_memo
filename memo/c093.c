#include <stdio.h>

void foo(){
        int a = 22;
        char b[3] = "d";
        printf("%d",a);
        printf("%s",b);
}

int main(){
        int N = 4;
        int res = 0;
        // scanf("%d", &N);

        for (int i=1; i<=N; i++) {
                res += i;
        }
        printf("%d\n", res);

        foo();

        return 0;
}

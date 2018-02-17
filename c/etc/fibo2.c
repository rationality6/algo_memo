#include <stdio.h>

int fibo(int n);

int cnt0 = 0, cnt1 = 0;


int fibo(int n) {
        if (n == 0)
                cnt0++;
        else if (n == 1)
                cnt1++;
        else
                return fibo(n - 1) + fibo(n - 2);
}

int main() {
        // int count, i, num;
        // scanf_s("%d", &count);
        // for (i = 0; i < count; i++) {
        //         scanf_s("%d", &num);
        //         fibo(num);
        //         printf("%d %d\n", cnt0, cnt1);
        //         cnt0 = 0, cnt1 = 0;
        // }
        return 0;
}

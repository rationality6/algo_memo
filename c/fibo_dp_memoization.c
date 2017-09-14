#include <stdio.h>


int main(){
        // int memory[];
        int a = Fibonacci(20);
        printf("%d",a);
}

int Fibonacci(int n)
{
        int fib[20];
        fib[0] = 1;
        fib[1] =1;
        for(int i = 2; i <= n; i++)
        {
                fib[i] = fib[i -2] + fib[i-1];
        }
        return fib[n];
}

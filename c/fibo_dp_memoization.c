#include <stdio.h>


int main(){
  // int memory[];

}

int Fibonacci(int n)
{
  int fib[20];
  fib[0] = 1;
  fib[1] =1;
  for(int i = 2;i <= n; i++)
  {
    fib[i] = fib[i -2] + fib[i-1];
  }
  return 0;
}

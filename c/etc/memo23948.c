#include <stdio.h>

void swap(int *a, int *b)
{
  int temp;
  temp = *a;
  *a = *b;
  *b = temp;
}

int main()
{
  int n = 4;
  int arr[] = {1, 4, 3, 2};
  int half_size = (n % 2 == 0) ? n / 2 : (n - 1) / 2;

  for (int i = 0; i < half_size; i++)
  {
    swap(&arr[i],&arr[(n - 1) - i]);
  }

  for (int i; i < n; i++)
  {
    printf("%d", arr[i]);
  }

  return 0;
}

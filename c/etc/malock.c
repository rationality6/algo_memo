#include <stdio.h>
#include <stdlib.h>

#define SIZE(_array) (sizeof(_array) / sizeof(_array[0]))
#define MIN(X, Y) (((X) < (Y)) ? (X) : (Y))
#define MAX(X, Y) (((X) > (Y)) ? (X) : (Y))

int main()
{
  int *arr_2;

  arr_2 = (int *)malloc(sizeof(int) * 5);
  // 메모리 할당, 배열의 크기만큼 할당하기 위해 5를 곱함

  for (int i = 0; i < 5; i++)
  {
    arr_2[i] = arr_1[i];
    printf("%d ", arr_2[i]);
  }

  printf("%d", MIN(1, 2));
  printf("%d", MAX(1, 2));
  return 0;
}
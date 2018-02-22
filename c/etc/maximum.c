#include <stdio.h>
#include <stdlib.h>

#define SIZE(_array) (sizeof(_array) / sizeof(_array[0]))
// #define LEN(_array) (sizeof(_array) / sizeof(_array[0]))
#define AGE (10 / 2)

int getMaxLength(int arr[], int n)
{
  int count = 0;
  int result = 0;
  for (int i = 0; i < n; i++)
  {
    if (arr[i] == 0)
      count = 0;
    else
    {
      count++;
      // result = max(result, count);
    }
  }
  return result;
}

int main()
{

  int arr[] = {1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1};

  printf("%d", SIZE(arr));
  // printf("%d", LEN(arr));
  // printf("%d", AGE);

  int arr_2 = (int *)malloc(sizeof(int) * 5);
  free(arr_2);
  return 0;
}
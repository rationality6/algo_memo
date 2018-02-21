#include <stdio.h>

int main()
{
  int array0[3][2] = {{1, 4}, {3, 4}, {3, 10}};

  int size = sizeof(array0) / sizeof(array0[0]);
  int sizeIn = sizeof(array0[0]) / size;

  printf("%d\n", size);
  printf("%d\n", sizeIn);

  for (int i = 0; i < size; i++)
  {
    for (int j = 0; j < sizeIn; j++)
    {
      printf("%d", array0[i][j]);
    }
  }
  return 0;
}

// int arr1[3][2] = {{1, 4}, {3, 4}, {3, 10}};
// int size = sizeof(arr1) / sizeof(arr1[0]);
// int sizeIn = sizeof(arr1[0]) / size;

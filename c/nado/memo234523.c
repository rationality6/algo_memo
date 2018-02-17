#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define LEN(_array) (sizeof(_array) / sizeof(_array[0]))

float getAverage(int arr[], int size)
{
  float avg;
  int sum;
  for (int i = 0; i < size; i++)
  {
    sum += arr[i];
  }
  avg = sum / size;
  return avg;
}

void sorting(int arr[])
{
  for (int i = 0; i < 2; i++)
  {
    printf("foo");
  }
}

int main()
{
  int balance[] = {6, 5, 38, 1, 332, 3};
  // // printf("%0.2f \n", getAverage(balance, 6));
  // int sort_array[] = {5, 4, 3, 2, 1};
  // // printf("%ld", LEN(sort_array));
  // // sorting(sort_array);

  // int array[100], n= 10, c, d, swap;

  // printf("Enter number of elements\n");

  // printf("Enter %d integers\n", n);

  // for (c = 0; c < (n - 1); c++)
  // {
  //   for (d = 0; d < n - c - 1; d++)
  //   {
  //     if (array[d] > array[d + 1]) /* For decreasing order use < */
  //     {
  //       swap = array[d];
  //       array[d] = array[d + 1];
  //       array[d + 1] = swap;
  //     }
  //   }
  // }

  // printf("Sorted list in ascending order:\n");

  for (int c = 0; c < n; c++)
  {
    printf("%d\n", array[c]);
  }

  return 0;
}

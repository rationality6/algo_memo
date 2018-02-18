#include <stdio.h>

void selection(int arr[], int size);
void swap(int *, int *);

int main()
{
  int arr0[] = {9, 8, 6, 5, 4, 3, 2, 1, 0};
  int size = sizeof(arr0) / sizeof(arr0[0]);

  selection(arr0, size);

  for (int i = 0; i < size; i++)
    printf("%d", arr0[i]);

  return 0;
}

void selection(int arr[], int size)
{
  for (int i = 0; i < size; i++)
  {
    int index = i;
    for (int j = i + 1; j < size; j++)
    {
      if (arr[j] < arr[index])
      {
        index = j;
      }
    }
    swap(&arr[i], &arr[index]);
  }
}

void swap(int *a, int *b)
{
  int temp;
  temp = *a;
  *a = *b;
  *b = temp;
}
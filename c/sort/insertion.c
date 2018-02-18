#include <stdio.h>

void insertion(int arr[], int size);

int main()
{
  int arr0[] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
  int size = sizeof(arr0) / sizeof(arr0[0]);

  insertion(arr0, size);

  return 0;
}

void insertion(int arr[], int size)
{
  for (int i = 1; i < size; i++)
  {
    int index = i;
    int current = arr[i];
    while (0 < index && current < arr[index - 1])
    {
      arr[index] = arr[index - 1];
      index--;
    }
    arr[index] = current;
  }

  for (int i = 0; i < size; i++)
    printf("%d", arr[i]);
}

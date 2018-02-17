// #include <stdio.h>

// void bubble_sort(int arr[], int count)
// {
//   int temp;
//   for (int i = 1; i < count; i++)
//   {
//     for (int j = 0; j < count - i; j++)
//     {
//       if (arr[j] > arr[j + 1])
//       {
//         temp = arr[j];
//         arr[j] = arr[j + 1];
//         arr[j + 1] = temp;
//       }
//     }
//   }
// }

// int main()
// {
//   int numArr[10] = {8, 4, 2, 5, 3, 7, 1, 6, 9, 0};
//   int size = sizeof(numArr) / sizeof(numArr[0]);
//   bubble_sort(numArr, size);

//   for (int i = 0; i < size; i++)
//   {
//     printf("%d\n", numArr[i]);
//   }

//   return 0;
// }

#include <stdio.h>

void bubble_sort(int arr[], int size);
void swap(int *a, int *b);

int main()
{
  int array0[] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
  int size = sizeof(array0) / sizeof(array0[0]);

  bubble_sort(array0, size);

  return 0;
}

void bubble_sort(int arr[], int size)
{
  int temp;
  for (int i = 1; i < size; i++)
  {
    for (int j = 0; j < size - i; j++)
    {
      if (arr[j] > arr[j + 1])
      {
        swap(&arr[j], &arr[j + 1]);
      }
    }
  }
  for (int i = 0; i < size; i++)
    printf("%d", arr[i]);
}

void swap(int *a, int *b)
{
  int temp;
  temp = *b;
  *b = *a;
  *a = temp;
}
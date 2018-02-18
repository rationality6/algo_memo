#include <stdio.h>

void merge(int arr[], int l, int m, int r)
{
  int i, j, k;
  int n1 = m - l + 1;
  int n2 = r - m;

  int L[n1], R[n2];

  for (i = 0; i < n1; i++)
  {
    L[i] = arr[l + i];
  }
  for (j = 0; j < n2; j++)
  {
    R[j] = arr[m + 1 + j];
  }

  i = 0;
  j = 0;
  k = l;

  while (i < n1 && j < n2)
  {
    if (L[i] <= R[j])
    {
      arr[k] = L[i];
      i++;
    }
    else
    {
      arr[k] = R[j];
      j++;
    }
    k++;
  }

  while (i < n1)
  {
    arr[k] = L[i];
    i++;
    k++;
  }
  while (j < n2)
  {
    arr[k] = R[j];
    j++;
    k++;
  }
}

void merge_sort(int arr[], int L, int R)
{
  if (L < R)
  {
    int m = L + (R - L) / 2;

    merge_sort(arr, L, m);
    merge_sort(arr, m + 1, R);

    merge(arr, L, m, R);
  }
}

int main()
{
  int array0[] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
  int size = sizeof(array0) / sizeof(array0[0]);

  merge_sort(array0, 0, size - 1);

  for (int i = 0; i < size; i++)
    printf("%d", array0[i]);

  return 0;
}

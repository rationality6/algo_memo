#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int get_random_number(int level)
{
  srand(time(NULL));
  return rand() % (level * 7) + 1;
}

int show_result(int answer, int input, int count)
{
  if (answer == input)
  {
    printf("Current!\n");
    count++;
  }
  else
  {
    printf("Wrong!\n");
  }
  return count;
}

int show_question(int level, int j, int k, int count)
{
  int answer = j * k;
  int input;
  printf("%dth password \n", level);
  printf("%d * %d = ? \n", j, k);
  scanf("%d", &input);
  show_result(answer, input, count);
  return count;
}

int main()
{
  printf("Game start \n");
  int count = 0;
  for (int i = 1; i <= 5; i++)
  {
    int num0 = get_random_number(i);
    int num1 = get_random_number(i);
    int answer;
    count = show_question(i, num0, num1, count);
  }
  printf("%d", count);

  return 0;
}

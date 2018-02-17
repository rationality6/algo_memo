#include <stdio.h>

int foo(int bar)
{
        return bar * 2;
}

int main()
{
        char *name = "John Smith";
        printf("asdf %s \n", name);

        int numbers[10];
        numbers[0] = 10;
        numbers[1] = 20;
        numbers[2] = 30;

        int i;
        for (i = 0; i < 4; i++)
        {
                printf("%d \n", numbers[i]);
                // printf("foo");
        }
        printf("%d", foo(3));

        return 0;
}

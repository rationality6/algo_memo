#include <stdio.h>
int main()
{
        int x = 10, y = -5;
        for(; x>6; x--)
        {
                for(; y<=0; y++)
                {
                        printf("%d%d",x, y);
                }
                printf("%d%d", x, y);
        }
}

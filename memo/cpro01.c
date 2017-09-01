#include <stdio.h>

void main(){
        static int a[5] = {'A','B','C','D','E'};
        for(int i = 0; i < 5; i++)
                printf("%c %d,", i++[a],a[i]);
}

#include <stdio.h>

int main(){
    int foo[10];
    int foobar = foo;

    printf("%p\n",&foo);
    printf("%d\n",foo==foobar);
    // printf("%d\n", foo == [9]);
    return 0;
}
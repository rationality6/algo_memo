#include <stdio.h>

void main(){
        char a[5] = {97,99,101,103,105};
        int i;
        for(int i = 0; i < 5; i=i+2){
          printf('%c',a[++i]);
        }
        printf(',%d',i);
}

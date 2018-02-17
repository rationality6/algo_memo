#include <stdio.h>

int cnt_0,cnt_1;
void fib(int n){
        if(n==0) {
                cnt_0++;
        }
        else if(n==1) {
                cnt_1++;
        }
        else{
                fib(n-1);
                fib(n-2);
        }
}

int main(){
        int T,N,i;

        scanf("%d",&T);

        for(i=0; i<T; i++) {
                scanf("%d",&N);
                cnt_0=0;
                cnt_1=0;

                fib(N);
                printf("%d %d\n",cnt_0,cnt_1);
        }
        return 0;
}

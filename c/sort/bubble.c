#include <stdio.h>
void one_to_n(n){
        for(int i = 0; i<n; i++) {
                printf("%d",i);
        }
}

void hello_world(){
        char text0[]="Hello world";
        printf("%s", text0);
}

void bubble_sort(int arr[],int count){
        int temp;
        for(int i = 1; i<count; i++) {
                for(int j = 0; j < count - i; j++) {
                        if(arr[j] < arr[j+1]) {
                                temp = arr[j];
                                arr[j] = arr[j+1];
                                arr[j+1] = temp;
                        }

                }
        }
}

int main(){
        // one_to_n(10);
        // hello_world();
        int numArr[10] = {8,4,2,5,3,7,1,6,9,0};
        int size = sizeof(numArr)/sizeof(int);
        bubble_sort(numArr,size);

        for(int i = 0; i<size; i++) {
                printf("%d\n",numArr[i]);
        }

        return 0;
}

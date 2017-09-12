#include <stdio.h>

int fibo(int num){
  if(num < 2){
    return num;
  }else{
    return fibo(num -1) + fibo(num-2);
  }
}

int main(){
  printf("%d",fibo(94));

}



// const fibo = n => {
//   if (n < 2) {
//     return n
//   } else {
//     return fibo(n - 1) + fibo(n - 2)
//   }
// }
//
// console.log(fibo(94));


int memory[];

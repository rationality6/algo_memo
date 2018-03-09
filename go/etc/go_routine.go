package main

import "fmt"

func work(n int) {
	for i := 0; i < n; i++ {
		fmt.Println(i)
	}
}

func for_loop(N int) {
	for i := 0; i < N; i++ {
		fmt.Println(i)
	}
}

func main() {

	// 일반 함수로 고루틴 생성
	go work(3)

	// 익명 함수로 고루틴 생성
	go func(n int) {
		for i := 0; i < n; i++ {
			fmt.Println(i)
		}
	}(3)
}

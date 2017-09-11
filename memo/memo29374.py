def fib(n):
    arr = [1, 1]
    for i in range(2, n + 1):
        print(i)
        arr[i] = arr[i - 2] + arr[i - 1]

    return arr[n]


print(fib(5))

arr = [1, 1]
arr.insert(0,3)
print(arr)

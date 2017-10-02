h, w = input().split()
h, w = int(h), int(w)
n = int(input())
arr = list()
for i in range(n):
    arr.append([])
    for j in range(4):
        arr[i].append(0)
for i in range(n):
    a = input().split()
    for j in range(4):
        arr[i][j] = int(a[i])
arr2 = list()
for i in range(h):
    arr2.append([])
    for j in range(w):
        arr2[i].append(0)
for i in range(n):
    if arr[i][1] == 0:
        for j in range(arr[i][0]):
            arr2[arr[i][2] - 1][arr[i][3] - 1] = 1
            arr[i][3] += 1
    else:
        for j in range(arr[i][0]):
            arr2[arr[i][2] - 1][arr[i][3] - 1] = 1
            arr[i][2] += 1
for i in range(h):
    for j in arr2[h]:
        print(j, end=' ')
    print()


input0 = 10
print(oct(input0)[2:])
binary = "000_0111_1010_1010_1010"
print(int(binary, 2))
input0 = 255
print(hex(input0))
print(int(input0))
print(int('13', 8))
print(oct(int('f', 16))[2:])
print(ord('A'))
print(ord('B'))


def sequence_sum(begin_number, end_number, step):
    result = 0
    for i in range(begin_number, end_number + 1, step):
        result += i
    return result


print(sequence_sum(2, 2, 2))


def partlist(LIST):
    result = []
    for i in range(1,len(LIST)):
        result.append((' '.join(LIST[:i]),' '.join(LIST[i:])))
    return result

# def partlist(arr):
#     return [(' '.join(arr[:i]), ' '.join(arr[i:])) for i in range(1, len(arr))]



alist = ["I", "wish", "I", "hadn't", "come"]
print(partlist(alist))

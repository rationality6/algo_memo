from random import randint

arr0 = [i for i in range(15)]

for i in range(0, len(arr0)):
    random_number = randint(0, len(arr0) - 1)
    temp = arr0[i]
    arr0[i] = arr0[random_number]
    arr0[random_number] = temp

print(arr0)

for i in range(1, len(arr0)):
    currentValue = arr0[i]
    position = i

    while 0 < position and currentValue < arr0[position - 1]:
        arr0[position] = arr0[position - 1]
        position -= 1

    arr0[position] = currentValue
print(arr0)

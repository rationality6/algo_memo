def result(N):
    count = 0
    queue = [int(i) for i in list(str(N))]

    while True:

        queue.append((queue[0] + queue[1]) % 10)
        queue.pop(0)

        count += 1
        if int("{}{}".format(queue[0], queue[1])) == N:
            return count

    return count


print(result(26))
print(result(23))
print(result(21))
print(result(32))

class test:
    def assert_equals(a, b):
        # pass
        print(a)
        # print(a == b)


def data_reverse(data):
    stack = []
    result = []
    for i in range((len(data) // 8)):
        stack.append(data[i * 8:(i + 1) * 8])
    for _ in range((len(data) // 8)):
        result.extend(stack.pop())
    return result


def data_reverse(data):
    return [b for a in range(len(data) - 8, -1, -8) for b in data[a:a + 8]]



data1 = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
data2 = [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1,
         1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]

test.assert_equals(data_reverse(data1), data2)

data3 = [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]
data4 = [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0]

# test.assert_equals(data_reverse(data3), data4)

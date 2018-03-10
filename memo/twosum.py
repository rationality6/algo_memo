def twoSum(nums, target):
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            # print(j)
            # if nums[i] - nums[j] == target:
            if nums[j] == target - nums[i]:
                print(i, j)
                # print(nums[i], nums[j])

array = [6, 7, 11, 15, 3, 6, 5, 3]
print(twoSum(array, 9))


def twosum(nums, target):
    lookup = dict(((v, i) for i, v in enumerate(nums)))
    print([i for i, v in enumerate(nums)])

    print(lookup.get(3))
    return next(((i + 1, lookup.get(target - v) + 1)
                 for i, v in enumerate(nums)
                 if lookup.get(target - v, i) != i), None)


array = [6, 7, 11, 15, 3, 6, 5, 3]
print(twosum(array, 6))


def twosum(nums, target):
    lookup = dict(((v, i) for i, v in enumerate(nums)))
    print(lookup)
    print([i for i, v in enumerate(nums)])

    print(lookup.get(3), 'lookup')

    for i, v in enumerate(nums):
        print(i, v)

    # return next(((i + 1, lookup.get(target - v) + 1)
    #              for i, v in enumerate(nums)
    #              if lookup.get(target - v, i) != i), None)


foobar = (6, 7, 11, 15, 3, 6, 5, 3)
print(twosum(foobar, 6))


dictionary = {
    "Name": "Harry0",
    "Age": 17,
    "Name": "foo",
    "Name": "Harry1",
    "Age": 22,
    "Name": "Harry2",
    "Name": "Harry3"
}
target = "Name"
print(dictionary[target])
print(dictionary.get(target))

def verifyItems(origItems, origPrices, items, prices):
    dict_orig = {}
    dict_moded = {}
    count = 0
    for key, value in zip(origItems, origPrices):
        dict_orig[key] = value
    for key, value in zip(items, prices):
        dict_moded[key] = value

    # print(dict_orig)
    # print(dict_moded)

    same_keys = len(set(dict_orig) & set(dict_moded))
    same_items = len(set(dict_orig.items()) & set(dict_moded.items()))

    return same_keys - same_items


a = ['rice', 'suger', 'wheat', 'cheese']
b = []

verifyItems(a)

dict0 = {3: 3}
print(dict0)
dict0[4] = 4
print(dict0)

list0 = []
for i in range(len(input())):
    list0.append(input())

print(list0)


def electionWinner(votes):
    from collections import Counter
    counted = Counter(votes)
    key_biggerst = 0
    name_list = []
    for key, val in counted.items():
        if key_biggerst < val:
            key_biggerst = val
            name_list = [key]
        elif(key_biggerst == val):
            name_list.append(key)

    print(sorted(name_list)[-1])
    return(sorted(name_list)[-1])


electionWinner(['blue', 'red', 'blue', 'yellow', 'blue', 'red'])


print(['a', 'b'][-1])


def maxDifference(a):
    answer = -1
    for i in range(1, len(a)):
        for j in range(0, i):
            if a[i] > a[j]:
                value = a[i] - a[j]
                if answer < value:
                    answer = value
    return answer


# list0 = [7, 2, 3, 10, 2, 4, 8, 1]
list0 = [6, 7, 9, 5, 6, 3, 2]

print(maxDifference(list0))


if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    tip_per_meal = meal_cost * (tip_percent * 0.01)
    tax_per_meal = meal_cost * (tax_percent * 0.01)
    total_cost = meal_cost + tip_per_meal + tax_per_meal
    print("The total meal cost is {} dollars.".format(round(total_cost)))


def move_zeros(L):
    for i in range(len(L)):
        print(i)

nums = [0, 1, 0, 3, 12]
should = [1, 3, 12, 0, 0]

print(move_zeros(nums) == should)

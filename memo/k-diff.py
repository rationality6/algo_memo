class Solution:
    def findPairs(nums, k):
        count = 0
        l = len(nums)
        for i in range(l):
            for j in range(i + 1, l):
                if abs(nums[i] - nums[j]) == k:
                    count += 1

        return count


list0 = [1, 2, 3, 4, 5]
list1 = [1, 5, 3, 4, 2]

k0 = 2
k1 = 3

print(Solution.findPairs(list0, k0))
print(Solution.findPairs(list1, k1))

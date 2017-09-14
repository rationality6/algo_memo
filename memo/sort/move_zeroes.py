# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
#
 

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    index = len(nums) - 1
    count = 0
    while index > count:
        if nums[count] == 0:
            nums.append(nums[count])
            print(count)
            nums.pop(count)
            index -= 1
        else:
            count += 1


num00 = [0, 1, 0, 3, 12]
print(num00)
moveZeroes(num00)
print(num00)

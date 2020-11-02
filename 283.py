'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
'''

def moveZeroes(self, nums: [int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    zero_num = 0
    for i in range(len(nums)):
        idx = i - zero_num
        if nums[idx] == 0:
            nums.pop(idx)
            nums.append(0)
            zero_num += 1
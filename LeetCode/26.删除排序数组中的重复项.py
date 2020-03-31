'''
@Author: your name
@Date: 2020-03-31 21:57:19
@LastEditTime: 2020-03-31 22:09:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/26.删除排序数组中的重复项.py
'''
#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        for ith in range(N):
            num = nums[ith]
            count = 0
            for jth in range(ith,N)
                tmp = nums[jth]
                if num != tmp:
                    break
                else:
                    count += 1
# @lc code=end


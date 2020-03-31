'''
@Author: your name
@Date: 2020-03-31 13:51:13
@LastEditTime: 2020-03-31 14:03:18
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/1.两数之和.py
'''
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)-1):
            spare = target - nums[i]
            if spare in nums[i+1:]:
                return [i, i+nums[i+1:].index(spare)+1]
            else:
                continue
        return None
# @lc code=end

if __name__ == "__main__":
    nums = [3,3]
    target = 6
    so = Solution()
    res = so.twoSum(nums,target)
'''
@Author: your name
@Date: 2020-04-01 15:59:44
@LastEditTime: 2020-04-01 17:40:28
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/35.搜索插入位置.py
'''
#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                continue
            else:
                return 0 if i == 0 else i
        return len(nums)


        
# @lc code=end
if __name__ == "__main__":
    so = Solution()
    so.searchInsert([1,3,5,6], 7)

'''
@Author: your name
@Date: 2020-04-01 15:59:44
@LastEditTime: 2020-04-01 21:58:43
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
                return i
        return len(nums)

    
    # def searchInsert(self,nums,target):
    #     head = 0
    #     tail = len(nums) - 1
        
    #     while True:
    #         _idx = round((head + tail) / 2)
    #         if nums[_idx] == target:
    #             return _idx
    #         elif nums[_idx] > target:
    #             tail = _idx
    #         else:
    #             head = _idx
    #         if head + 1 == tail or head == tail:
    #             break
    #     for i in [head,tail]:
    #         if nums[i] == target:
    #             return i
    #         elif nums[i] < target:
    #             continue
    #         else:
    #             return i
    #     return tail + 1
# @lc code=end
if __name__ == "__main__":
    so = Solution()
    print(so.searchInsert([1],0))

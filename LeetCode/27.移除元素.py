'''
@Author: your name
@Date: 2020-04-01 09:48:13
@LastEditTime: 2020-04-01 13:48:35
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/27.移除元素.py
'''
#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums, val):
        _idx = 0
        ith = 0
        N = len(nums)
        while ith < N:
            ith_num = nums[ith]
            removeNum = 0

            for jth in range(ith+1,N):
                if nums[jth] == val:
                    removeNum += 1
                else:
                    break
            
            ith += 1 if removeNum == 0 else removeNum + 1
            if ith_num != val: 
                nums[_idx] = ith_num
                _idx += 1
        return _idx


# @lc code=end

if __name__ == "__main__":
    so = Solution()
    so.removeElement([3,2,2,3],3)

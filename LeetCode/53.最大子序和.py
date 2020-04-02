'''
@Author: your name
@Date: 2020-04-02 14:49:54
@LastEditTime: 2020-04-02 16:48:46
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/53.最大子序和.py
'''
#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums) -> int:
        N = len(nums)
        # dp = [ [0 for i in range(N)] for j in range(N)]

        # for i in range(N):
        #     for j in range(N):
        #         if i == j:
        if N == 1: return nums[0]
        maximum = nums[0]
        
        for ith in range(N):
            s = nums[ith]
            for jth in range(ith+1,N):
                s += nums[jth]
                maximum = s if s > maximum else maximum
            maximum = s if s > maximum else maximum
        return maximum
            
                    
                
                    
# @lc code=end

if __name__ == "__main__":
    so = Solution()
    so.maxSubArray([-2,1])
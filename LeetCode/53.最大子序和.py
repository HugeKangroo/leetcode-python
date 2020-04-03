'''
@Author: your name
@Date: 2020-04-02 14:49:54
@LastEditTime: 2020-04-03 09:15:26
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
# class Solution:
    # def maxSubArray(self, nums) -> int:
    #     N = len(nums)
    #     if N == 1: return nums[0]
    #     maximum = nums[0]
        
    #     for ith in range(N):
    #         s = nums[ith]
    #         maximum = s if s > maximum else maximum
    #         for jth in range(ith+1,N):
    #             s += nums[jth]
    #             maximum = s if s > maximum else maximum
    #     return maximum
    


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        #递归终止条件
        if n == 1:
            return nums[0]
        else:
            #递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            #递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])
        
        #计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        #在中间的情况下，从中间往两端推
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        #返回三个中的最大值
        return max(max_right,max_left,max_l+max_r)

    # def maxSubArray(self, A):
    #     if not A:
    #         return 0

    #     curSum = maxSum = A[0]
    #     for num in A[1:]:
    #         curSum = max(num, curSum + num)
    #         maxSum = max(maxSum, curSum)

    #     return maxSum
# @lc code=end

if __name__ == "__main__":
    so = Solution()
    so.maxSubArray([-2,1])
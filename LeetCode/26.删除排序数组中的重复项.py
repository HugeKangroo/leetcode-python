'''
@Author: your name
@Date: 2020-03-31 21:57:19
@LastEditTime: 2020-03-31 22:29:04
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
    def removeDuplicates(self, nums):
        N = len(nums)
        _idx = 0
        ith = 0
        while ith < N:
            num = nums[ith]
            repeatNum = 0
            for jth in range(ith+1,N):
                if nums[jth] == num:
                    repeatNum += 1
                else:
                    break
            nums[_idx] = num
            _idx += 1
            ith += repeatNum + 1
        return _idx
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp = [[0] * len(prices)
        dp =[[0,0] for i in range(len(prices))]

        for i in range(len(prices)):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[0]
            else:
                dp[i][0] = max(dp[i-1][1]+prices[i],dp[i-1][0])#第i天非持有状态的最大利润
                dp[i][1] = max(-prices[i],dp[i-1][1])#第i天持有状态的最大利润,
                #不能使用dp[i-1][0]-prices[i]，因为只可购买一次
        return dp[-1][0]

# @lc code=end

if __name__ == "__main__":
    so = Solution()
    so.removeDuplicates([1,1,2])
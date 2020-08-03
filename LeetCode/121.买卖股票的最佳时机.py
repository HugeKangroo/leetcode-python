'''
Author: your name
Date: 2020-08-03 17:40:39
LastEditTime: 2020-08-03 17:40:55
LastEditors: your name
Description: In User Settings Edit
FilePath: /Algrithm/LeetCode/121.买卖股票的最佳时机.py
'''
#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
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


'''
@Author: your name
@Date: 2020-06-29 14:58:54
@LastEditTime: 2020-07-06 17:39:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/96.不同的二叉搜索树.py
'''
#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [ 0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2,n+1):
            for j in range(i+2,n+1):
                dp[i] += dp[i+1]

# @lc code=end


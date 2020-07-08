'''
@Author: your name
<<<<<<< HEAD
@Date: 2020-07-05 01:20:02
@LastEditTime: 2020-07-08 20:01:02
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /LeetCode/96.不同的二叉搜索树.py
=======
@Date: 2020-06-29 14:58:54
@LastEditTime: 2020-07-06 17:42:36
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/96.不同的二叉搜索树.py
>>>>>>> fd1b570bd7358559f88a022eaf321020fb667395
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
            for j in range(i+1,n+1):
                dp[i] += dp[j-1] * dp[n-j]

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(3))
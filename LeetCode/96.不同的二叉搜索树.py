'''
@Author: your name
@Date: 2020-07-05 01:20:02
@LastEditTime: 2020-07-05 01:28:41
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /LeetCode/96.不同的二叉搜索树.py
'''
#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [ 0 for i in range(n+1)]
        dp[0] = 1 ## empty tree
        dp[1] = 1 ## tree with one node 
        for i in range(2,n+1):
            for j in range(i+1,n+1):
               dp[i] +=  dp[j-1] * dp[]

        return dp[n]

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.numTrees(3))
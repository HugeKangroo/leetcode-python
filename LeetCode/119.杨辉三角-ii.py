'''
@Author: your name
@Date: 2020-07-12 00:21:26
@LastEditTime: 2020-07-12 00:22:39
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/119.杨辉三角-ii.py
'''
#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (61.24%)
# Likes:    160
# Dislikes: 0
# Total Accepted:    58.9K
# Total Submissions: 96.1K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 3
# 输出: [1,3,3,1]
# 
# 
# 进阶：
# 
# 你可以优化你的算法到 O(k) 空间复杂度吗？
# 
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int):
        dp = [[ 0 for i in range(rowIndex+1)] for j in range(rowIndex+1)]

        for i in range(rowIndex+1):
            for j in range(rowIndex+1):
                if (i == 0 and j==0) or (i==rowIndex and j== rowIndex):
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                    
        return  dp[rowIndex]
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    s.getRow(5)


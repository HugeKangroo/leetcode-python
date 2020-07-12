'''
@Author: your name
@Date: 2020-07-12 15:25:14
@LastEditTime: 2020-07-12 15:25:20
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/70.爬楼梯.py
'''
#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (49.85%)
# Likes:    1125
# Dislikes: 0
# Total Accepted:    238.7K
# Total Submissions: 477.6K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 注意：给定 n 是一个正整数。
# 
# 示例 1：
# 
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 
# 示例 2：
# 
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.mem = {}
        
    def climbStairs(self, n: int) -> int:
        if n in self.mem.keys():
            return self.mem[n]
        if n == 1:res = 1
        elif n == 2:res = 2
        else:
            res = 0
            for i in range(2):
                res += self.climbStairs(n-i-1)
        self.mem[n] = res
        return res
# @lc code=end


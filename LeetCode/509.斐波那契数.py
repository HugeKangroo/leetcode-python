'''
@Author: your name
@Date: 2020-07-12 15:14:03
@LastEditTime: 2020-07-12 15:14:11
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/509.斐波那契数.py
'''
#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#
# https://leetcode-cn.com/problems/fibonacci-number/description/
#
# algorithms
# Easy (66.68%)
# Likes:    139
# Dislikes: 0
# Total Accepted:    63.3K
# Total Submissions: 94.9K
# Testcase Example:  '2'
#
# 斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
# 
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 
# 
# 给定 N，计算 F(N)。
# 
# 
# 
# 示例 1：
# 
# 输入：2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
# 
# 
# 示例 2：
# 
# 输入：3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
# 
# 
# 示例 3：
# 
# 输入：4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3.
# 
# 
# 
# 
# 提示：
# 
# 
# 0 ≤ N ≤ 30
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.mem = {}
        
    def fib(self, N: int) -> int:
        if N in self.mem.keys():
            return self.mem[N]
        
        if N == 0:
            res = 0
        elif N == 1:
            res = 1
        else:
            res = self.fib(N-1) + self.fib(N-2)
        self.mem[N] = res
        return res
# @lc code=end


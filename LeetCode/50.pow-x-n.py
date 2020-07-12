'''
@Author: your name
@Date: 2020-07-12 15:59:35
@LastEditTime: 2020-07-12 16:00:39
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/50.pow-x-n.py
'''
#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode-cn.com/problems/powx-n/description/
#
# algorithms
# Medium (35.98%)
# Likes:    438
# Dislikes: 0
# Total Accepted:    106.8K
# Total Submissions: 296.1K
# Testcase Example:  '2.00000\n10'
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
# 
# 示例 1:
# 
# 输入: 2.00000, 10
# 输出: 1024.00000
# 
# 
# 示例 2:
# 
# 输入: 2.10000, 3
# 输出: 9.26100
# 
# 
# 示例 3:
# 
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 说明:
# 
# 
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
# 
# 
#

# @lc code=start
class Solution:
    def __init__(self):
        self.mem = {}
    
    def myPow(self, x: float, n: int) -> float:  
        abs_n = abs(n)
        res = self.recursive(x,abs_n)
        return res if n >= 0 else 1.0 /res

    
    def recursive(self,x,n):
        if n in self.mem.keys():return self.mem[n]
        if n == 0:
            self.mem[n] = 1
            return 1
        else:
            res = x * self.myPow(x,n-1)
            self.mem[n] = res
            return res
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    s.myPow(2,22)

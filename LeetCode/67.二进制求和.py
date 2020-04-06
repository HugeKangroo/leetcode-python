'''
@Author: your name
@Date: 2020-04-04 14:12:53
@LastEditTime: 2020-04-05 12:34:19
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/67.二进制求和.py
'''
#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (52.33%)
# Likes:    332
# Dislikes: 0
# Total Accepted:    73.4K
# Total Submissions: 140.2K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 
# 输入为非空字符串且只包含数字 1 和 0。
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0:return b
        if len(b) == 0:return a
        
        if a[-1] == "1" and b[-1] == "1":
            return self.addBinary(self.addBinary(a[:-1],b[:-1]),"1") + "0"
        elif a[-1] == "0" and b[-1] == "0":
            return self.addBinary(a[:-1],b[:-1]) + "0"
        else:
            return self.addBinary(a[:-1],b[:-1]) + "1"



        
        
# @lc code=end


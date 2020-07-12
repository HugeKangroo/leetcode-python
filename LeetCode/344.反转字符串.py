'''
@Author: your name
@Date: 2020-07-12 00:48:06
@LastEditTime: 2020-07-12 00:48:23
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/344.反转字符串.py
'''
#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#
# https://leetcode-cn.com/problems/reverse-string/description/
#
# algorithms
# Easy (70.57%)
# Likes:    254
# Dislikes: 0
# Total Accepted:    156.9K
# Total Submissions: 221.8K
# Testcase Example:  '["h","e","l","l","o"]'
#
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
# 
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
# 
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
# 
# 
# 
# 示例 1：
# 
# 输入：["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]
# 
# 
# 示例 2：
# 
# 输入：["H","a","n","n","a","h"]
# 输出：["h","a","n","n","a","H"]
# 
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def recursive(s,start,end):
            if start==end:
                pass
            elif end - start == 1:
                s[start],s[end] = s[end],s[start]
            else:
                s[start],s[end] = s[end],s[start]
                recursive(s,start+1,end-1)
        recursive(s,0,len(s)-1)
# @lc code=end


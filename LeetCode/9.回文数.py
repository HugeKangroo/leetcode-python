'''
@Author: your name
@Date: 2020-03-31 17:21:48
@LastEditTime: 2020-03-31 17:23:32
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/9.回文数.py
'''
#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x2str = str(x)
        revd = x2str[::-1]

        if x2str == revd:
            return True
        else:
            return False
# @lc code=end


'''
@Author: your name
@Date: 2020-04-01 10:32:26
@LastEditTime: 2020-04-01 12:09:31
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/28.实现-str-str.py
'''
#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        for ith in range(len(haystack)):
            repeatNum = 0
            for jth in range(len(needle)):
                if haystack[ith] == needle[jth]:
                    repeatNum += 1
                else:
                    break
            if repeatNum == len(needle):
                return ith
            else:
                continue
        return -1

# @lc code=end


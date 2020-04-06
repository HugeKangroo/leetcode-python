'''
@Author: your name
@Date: 2020-04-06 12:20:30
@LastEditTime: 2020-04-06 13:07:35
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/5.最长回文子串.py
'''
#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (29.15%)
# Likes:    1959
# Dislikes: 0
# Total Accepted:    225.1K
# Total Submissions: 770.2K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        if len_s == 0:return -1
        elif len_s == 1:return s
        else:
            dp = [ i for i in s]
            for i in range(1,len_s-1):
                tmp = dp[i-1] + s[i]
                if tmp == tmp[::-1]:
                    dp[i] = tmp
                else:
                    dp[i] = s[i]
        return dp[-1]  
                    
        
# @lc code=end

if __name__ == "__main__":
    so = Solution()
    so.longestPalindrome("babad")
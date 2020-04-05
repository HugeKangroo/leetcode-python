'''
@Author: your name
@Date: 2020-04-04 13:06:17
@LastEditTime: 2020-04-04 13:42:13
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/58.最后一个单词的长度.py
'''
#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.86%)
# Likes:    183
# Dislikes: 0
# Total Accepted:    79.4K
# Total Submissions: 241.4K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
# 
# 如果不存在最后一个单词，请返回 0 。
# 
# 说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。
# 
# 
# 
# 示例:
# 
# 输入: "Hello World"
# 输出: 5
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # if s == "" or s == " ": return 0
        # seqs = s.split(" ")
        # for seq in seqs[::-1]:
        #     if seq == "":
        #         continue
        #     else:
        #         return len(seq)
        # return 0
        ls = len(s)
        tail = ls - 1 
        while tail >= 0:
            if s[tail] == " ":
                tail -= 1
                continue
            else:
                break
        # if tail == 0: return 0
        head = tail
        while head >= 0:
            if s[head] == " ":
                break
            else:
                head -= 1
                continue
        return tail - head 

# @lc code=end

if __name__ == "__main__":
    so = Solution()
    so.lengthOfLastWord("Hello World")
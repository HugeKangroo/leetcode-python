'''
@Author: your name
@Date: 2020-03-31 17:55:38
@LastEditTime: 2020-03-31 18:03:32
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/14.最长公共前缀.py
'''
#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        findShortStr = lambda listStr : sorted(listStr,key =lambda x:len(x))

        baseStr = findShortStr(strs)[0]

        res = ""
        for i,char in enumerate(baseStr):
            if 
# @lc code=end
if __name__ == "__main__":
    # findShortStr = lambda listStr : sorted(listStr,key =lambda x:len(x))

    # strs = ["124444444443","123123","123123"]
    # res = findShortStr(strs)
    print()

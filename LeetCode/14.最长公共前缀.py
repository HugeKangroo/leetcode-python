'''
@Author: your name
@Date: 2020-03-31 17:55:38
@LastEditTime: 2020-03-31 19:58:27
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
    def longestCommonPrefix(self, strs):
        findShortStr = lambda listStr : sorted(listStr,key =lambda x:len(x))
        res = ""
        if len(strs) == 0:return res
        shortest = findShortStr(strs)[0]
        for i in range(len(shortest)):
            char_i = shortest[i]
            tmp = [char_i for string in strs]
            if tmp  == [string[i] for string in strs]:
                res += char_i
            else:
                break
        return res

# @lc code=end
if __name__ == "__main__":
    so = Solution()
    so.longestCommonPrefix(["aca","cba"])
    print()

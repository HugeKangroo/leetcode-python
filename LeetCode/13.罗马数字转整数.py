'''
@Author: your name
@Date: 2020-03-31 17:28:10
@LastEditTime: 2020-03-31 17:48:44
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/13.罗马数字转整数.py
'''
#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        value_map = {"I":1,"V":5,"X":10, \
                    "L":50,"C":100,"D":500, \
                    "M":1000}
        rev_s = s[::-1]
        res = 0
        for i in range(len(rev_s)):
            if i > 0:
                if rev_s[i] == "I" and rev_s[i-1] in ["V","X"] :
                    res += -1 * value_map[rev_s[i]]
                    continue
                elif rev_s[i] == "X" and rev_s[i-1] in ["L","C"]:
                    res += -1 * value_map[rev_s[i]]
                    continue
                elif rev_s[i] == "C" and rev_s[i-1] in ["D","M"]:
                    res += -1 * value_map[rev_s[i]]
                    continue
                
            res += value_map[rev_s[i]]
        return res 

# @lc code=end

if __name__ == "__main__":
    so = Solution()
    so.romanToInt("III")

'''
@Author: your name
@Date: 2020-03-31 10:46:24
@LastEditTime: 2020-03-31 13:49:08
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/290.单词规律.py
'''
#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        indexOf = lambda x,y:  [ a for a,b in enumerate(x) if b == y]
        words = str.split(" ")
        # set_pattern = list(set(pattern))
        # set_str = set(words)
        
        p_map = list(map(lambda x:indexOf(pattern,x),pattern))
        s_map = list(map(lambda x:indexOf(words,x),words))
        if p_map == s_map:
            return True
        else:
            return False
# @lc code=end

if __name__ == "__main__":
    pattern = "abba"
    string = "dog cat cat dog"
    so = Solution()
    res = so.wordPattern(pattern,string)
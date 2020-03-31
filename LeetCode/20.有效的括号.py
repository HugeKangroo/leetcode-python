'''
@Author: your name
@Date: 2020-03-31 20:08:47
@LastEditTime: 2020-03-31 21:02:44
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/20.有效的括号.py
'''
#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        left_type = ["(","{","["]
        right_type = [")","}","]"]
        table = []
        if len(s) % 2 != 0: return False
        for ith,char in enumerate(s):
            if char in left_type:
                _id = left_type.index(char)
                table.append(_id)
            elif char in right_type:
                _id = right_type.index(char)
                if len(table) == 0:
                    return False
                else:
                    if table[-1] == _id:
                        table = table[:-1]
                    else:
                        return False
        # sum_row = [ sum(t) for t in table]
        if len(table) == 0:
            return True
        else:
            return False

        
# @lc code=end

if __name__ == "__main__":
    so = Solution()
    # so.isValid("{[]}")
    so.isValid("()")
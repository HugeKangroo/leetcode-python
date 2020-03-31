'''
@Author: your name
@Date: 2020-03-31 16:38:27
@LastEditTime: 2020-03-31 17:20:23
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/7.整数反转.py
'''
#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # noZero = lambda x: [ i for i,item in x if item <> "0"]
        if x == 0 : return x
        
        minus = -1 if x < 0 else 1
        abs_x = abs(x)

        # if abs_x > 2**31 - 1 : return 0
        rev = str(abs_x)[::-1]
        ids = [i for i,item in enumerate(rev) if item != "0"]
        res = int(rev[ids[0]:])
        res = res if res <= 2**31-1 else 0
        return minus*res
# @lc code=end

if __name__ == "__main__":
    so = Solution()
    res = so.reverse(1534236469)
    print(res)
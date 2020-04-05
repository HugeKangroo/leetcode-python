'''
@Author: your name
@Date: 2020-04-04 13:42:32
@LastEditTime: 2020-04-04 14:11:06
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/66.加一.py
'''
#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (43.66%)
# Likes:    451
# Dislikes: 0
# Total Accepted:    137.3K
# Total Submissions: 314.2K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
# 
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
# 
# 
# 示例 2:
# 
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
# 
# 
#

# @lc code=start
class Solution:
    def plusOne(self, digits):
        ls = len(digits)
        digits[-1] += 1
        last = 0
        for i in range(ls-1,-1,-1):
            digits[i] += last
            if digits[i] > 9:
                digits[i] -= 10
                last = 1
            else:
                last = 0
        if last == 1:return [1] + digits
        else: return digits


# @lc code=end
if __name__ == "__main__":
    ls = 10
    # for i in range(ls-1,-1,-1):
    #     print(i)
    so = Solution()
    so.plusOne([9])

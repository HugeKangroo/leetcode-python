'''
@Author: your name
@Date: 2020-07-11 22:32:37
@LastEditTime: 2020-07-11 23:13:14
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/118.杨辉三角.py
'''
#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (66.66%)
# Likes:    327
# Dislikes: 0
# Total Accepted:    89.1K
# Total Submissions: 133.5K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) :
        def generate_(level):
            if level == 1:

                return [[1]]
            # elif level == 2:
            #     return [generate_(level-1),[1,1]]
            else:
                res = generate_(level-1)
                middle = []
                for i in range(len(res[-1])-1):
                    middle.append(res[-1][i] + res[-1][i+1])
                
                return [ele for ele in res]+[[1] + middle + [1]]
        return generate_(numRows)
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))

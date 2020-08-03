'''
@Author: your name
@Date: 2020-07-29 14:08:54
LastEditTime: 2020-08-03 17:40:07
LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/和为s的连续正数序列.py
'''
# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列

class Solution:
    def findContinuousSequence(self, target: int):
        s = 1
        e = 1
        tol = 0
        res = []
        while s <= target // 2:
            if tol < target:
                tol += e
                e += 1
            elif tol > target:
                tol -= s
                s += 1
            else:
                res.append(list(range(s,e)))
                tol -= s
                s += 1
        return res
if __name__ == "__main__":
    s = Solution()
    s.findContinuousSequence(10)
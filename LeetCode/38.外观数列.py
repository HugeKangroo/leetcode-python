'''
@Author: your name
@Date: 2020-04-02 08:58:28
@LastEditTime: 2020-04-02 12:04:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/38.外观数列.py
'''
#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 外观数列
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        last = "1"
        for i in range(1,n):
            
            for head in range(0,len(last))：
                for tail in range(head+1,len(last)):
                    if 
            

# @lc code=end


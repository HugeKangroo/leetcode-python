'''
@Author: your name
@Date: 2020-04-02 08:58:28
@LastEditTime: 2020-04-02 14:46:12
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
        tmp = "1"
        for i in range(1,n):
            head = 0
            say = ""
            while head < len(tmp):
                count = 0
                tail = head + 1
                while tail < len(tmp):
                    if tmp[head] == tmp[tail]:
                        count += 1
                    else:
                        break
                    tail += 1
                say += str(count + 1) + tmp[head]
                head += count + 1
            tmp = say
        return tmp

# @lc code=end

if __name__ == "__main__":
    so = Solution()
    so.countAndSay(6)
'''
@Author: your name
@Date: 2020-04-01 10:32:26
@LastEditTime: 2020-04-01 15:42:10
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/28.实现-str-str.py
'''
#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
    #     H = len(haystack)
    #     N = len(needle)
    #     if N == 0: return 0
    #     if N > H: return -1
        
    #     dp = [[ 0 for i in range(H)] for j in range(N)]
        
    #     for nth in range(N):
    #         for hth in range(H):
    #             if needle[nth] == haystack[hth]:
    #                 if nth > 0 and hth > 0:
    #                     dp[nth][hth] += dp[nth-1][hth-1] + 1

    #                 else:
    #                     dp[nth][hth] = 1
                        
    #             if dp[nth][hth] == N:
    #                 return hth - N + 1
    #     return -1

        def strStr(self, haystack: str, needle: str) -> int:
            N = len(haystack)
            M = len(needle)
            if M == 0: return 0
            if M > N: return -1
            ith = 0
            while ith < N:
                cnum = 0
                if ith + M > N: return -1
                for jth in range(M):
                    h_char = haystack[ith+jth]
                    n_char = needle[jth]
                    if n_char == h_char:
                        cnum += 1
                    else:
                        break
                if cnum == M:
                    return ith
                else:
                    ith += 1 
            return -1



# @lc code=end


if __name__ == "__main__":
    so = Solution()
    print(so.strStr(haystack = "a", needle = "a"))


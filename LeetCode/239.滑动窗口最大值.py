#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        s = 0
        e = s+k 
        # max_val = float("-inf")
        n = len(nums)
        res = []
        while e <= n:
            res.append(max(nums[s:e]))
            s += 1
            e = s + k
        return res
# @lc code=end


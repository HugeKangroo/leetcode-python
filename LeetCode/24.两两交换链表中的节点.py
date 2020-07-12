'''
@Author: your name
@Date: 2020-07-12 01:29:19
@LastEditTime: 2020-07-12 01:29:36
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/24.两两交换链表中的节点.py
'''
#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (65.94%)
# Likes:    545
# Dislikes: 0
# Total Accepted:    123K
# Total Submissions: 185.9K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例:
# 
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            rest = self.swapPairs(head.next.next)
            head, head.next = head.next,head
            head.next.next = rest
            return head
# @lc code=end


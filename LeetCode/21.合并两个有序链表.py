'''
@Author: your name
@Date: 2020-03-31 21:04:41
@LastEditTime: 2020-03-31 21:54:31
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/21.合并两个有序链表.py
'''
#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return
        elif l1 is not None and l2 is not None:
            if l1.val >= l2.val:
                next_node1 = l1 # 保留较大节点
                next_node2 = l2.next
                val = l2.val # 保留较小的值
            else:
                next_node1 = l2
                next_node2 = l1.next
                val = l1.val
            cur = ListNode(val)
            cur.next = self.mergeTwoLists(next_node1,next_node2)
            return cur
        elif l1 is None and l2 is not None:
            val = l2.val
            cur = ListNode(val)
            cur.next = self.mergeTwoLists(None,l2.next)
            return cur
        else:
            val = l1.val
            cur = ListNode(val)
            cur.next = self.mergeTwoLists(l1.next,None)
            return cur

# @lc code=end


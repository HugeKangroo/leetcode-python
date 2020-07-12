'''
@Author: your name
@Date: 2020-07-12 00:50:33
@LastEditTime: 2020-07-12 14:54:02
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/206.反转链表.py
'''
#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (69.50%)
# Likes:    1083
# Dislikes: 0
# Total Accepted:    276.6K
# Total Submissions: 396.6K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None : return None
        elif head.next is None: return head
        else:
            nex = self.reverseList(head.next) # 此时head的内存顺序未改变
            head.next.next = head # 将当前head连接到head.next.next之后以改变nex中节点顺序
            head.next = None#避免形成环路
            return nex

    def reverseList2(self,head:ListNode) -> ListNode:
        # stack = []
        res = None
        while(True):
            if head.next is None:
                head.next = res
                res = head
                break
            else:
                if res is None:
                    res = ListNode(head.val)
                else:
                    cur = ListNode(head.val)
                    cur.next = res
                    res = cur
                head = head.next
        return res

    def reverseList3(self,head:ListNode) -> ListNode:
        # stack = []
        res = None
        while(True):
            if head is None:
                break
            else:
                temp = head.next ## 记录head.next节点
                head.next = res  ## 修改head的next节点
                res = head # 修改res
                head = temp # 按原temp迭代
        return res

# @lc code=end

def buildListNodes(nodes,val):
    if nodes is None:
        return ListNode(val)
    else:
        nodes.next = buildListNodes(nodes.next,val)
        return nodes

if __name__ == "__main__":
    in_value = [1,2,3,4,5]
    nodes = None
    
    # for i in in_value:
    #     if nodes is None:
    #         nodes = ListNode(i)
    #     else:
    #         cur_node = ListNode(i)
    #         cur_node.next = nodes
    #         nodes = cur_node
    for i in in_value:
        nodes = buildListNodes(nodes,i)
    #     if nodes is None:
    #         nodes = ListNode(i)
    #     else:
    #         cur_node = ListNode(i)
    #         cur_node.next = nodes
    #         nodes = cur_node
    s = Solution()
    
    res = s.reverseList3(nodes)
    print()



'''
@Author: your name
@Date: 2020-03-31 14:04:46
@LastEditTime: 2020-03-31 16:15:41
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/2.两数相加.py




'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def addNumbers(l1,l2,add=0):
            val = None
            next_add = 0
            next_node = False  
            if l1 is None and l2 is not None:
                val = l2.val + add
                next1 = None
                next2 = l2.next
                
            elif l2 is None and l1 is not None:
                val = l1.val + add
                next1 = l1.next
                next2 = None 

            elif l2 is not None and l1 is not None:
                val = l1.val + l2.val + add
                next1 = l1.next
                next2 = l2.next
                
            elif l2 is None and l1 is None and add != 0:
                next1 = None
                next2 = None 
                val = add
            else:
                return 

            if val >= 10:
                val = val - 10
                next_add = 1
            else:
                val = val
                next_add = 0
            
            if next1 is not None or next2 is not None or next_add != 0:
                next_node = True
            else:
                next_node = False


            if next_node:
                node = ListNode(val)
                node.next = addNumbers(next1,next2,next_add)
                return node
            else:
                node = ListNode(val)
                # node.next = None 
                return node
        return addNumbers(l1,l2)

# @lc code=end


if __name__ == "__main__":
    


    # l13 = ListNode(6)
    # l12 = ListNode(1)
    # l12.next = l13

    # l11 = ListNode(9)
    # l11.next = l12
    l1 = ListNode(5)

    l2 = ListNode(5)

    so = Solution()
    res = so.addTwoNumbers(l1,l2)
    print()
    # l23 = ListNode(4)
    # l22 = ListNode(6)
    # l22.next = l23
    # l21 = ListNode(5)
    # l21.next = l22
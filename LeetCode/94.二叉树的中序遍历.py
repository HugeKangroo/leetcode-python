'''
@Author: your name
@Date: 2020-07-05 01:20:02
@LastEditTime: 2020-07-08 21:55:06
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /LeetCode/94.二叉树的中序遍历.py
'''
#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: return []
        else:
            left = self.inorderTraversal(root.left)
            right = self.inorderTraversal(root.right)
            return left + [root.val] + right
# @lc code=end


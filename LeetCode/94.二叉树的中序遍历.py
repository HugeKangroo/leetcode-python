'''
@Author: your name
@Date: 2020-06-27 22:28:10
@LastEditTime: 2020-06-27 22:43:56
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /LeetCode/94.二叉树的中序遍历.py
'''
#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (70.76%)
# Likes:    543
# Dislikes: 0
# Total Accepted:    178.9K
# Total Submissions: 249.1K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 输出: [1,3,2]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
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


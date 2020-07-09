'''
@Author: your name
@Date: 2020-07-09 23:16:56
@LastEditTime: 2020-07-09 23:30:44
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/99.恢复二叉搜索树.py
'''
#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#
# https://leetcode-cn.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (57.47%)
# Likes:    243
# Dislikes: 0
# Total Accepted:    20.7K
# Total Submissions: 35.9K
# Testcase Example:  '[1,3,null,null,2]'
#
# 二叉搜索树中的两个节点被错误地交换。
# 
# 请在不改变其结构的情况下，恢复这棵树。
# 
# 示例 1:
# 
# 输入: [1,3,null,null,2]
# 
# 1
# /
# 3
# \
# 2
# 
# 输出: [3,1,null,null,2]
# 
# 3
# /
# 1
# \
# 2
# 
# 
# 示例 2:
# 
# 输入: [3,1,4,null,null,2]
# 
# ⁠ 3
# ⁠/ \
# 1   4
# /
# 2
# 
# 输出: [2,1,4,null,null,3]
# 
# ⁠ 2
# ⁠/ \
# 1   4
# /
# ⁠ 3
# 
# 进阶:
# 
# 
# 使用 O(n) 空间复杂度的解法很容易实现。
# 你能想出一个只使用常数空间的解决方案吗？
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def buildTree(root,val):
            if root is None:
                root = TreeNode(val)
                return root
            else:
                if val < root.val:
                    root.left = buildTree(root.left,val)
                    return root
                elif val > root.val:
                    root.right = buildTree(root.right,val)
                    return root
                
# @lc code=end


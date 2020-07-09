'''
@Author: your name
@Date: 2020-07-08 21:30:52
@LastEditTime: 2020-07-09 22:52:19
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /LeetCode/98.验证二叉搜索树.py
'''
#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (31.52%)
# Likes:    649
# Dislikes: 0
# Total Accepted:    138.1K
# Total Submissions: 436.1K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 
# 假设一个二叉搜索树具有如下特征：
# 
# 
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 示例 1:
# 
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
# 
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
    
    def __init__(self):
        self.pre = float("-inf")
        
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            if not self.isValidBST(root.left): # 排除左树
                return False 
            if root.val <= self.pre: # 排除中点（非升序和相等项）
                return False 
            self.pre = root.val
            return self.isValidBST(root.right) # 排除右树
# @lc code=end


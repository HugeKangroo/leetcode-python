'''
@Author: your name
@Date: 2020-06-30 11:12:07
@LastEditTime: 2020-07-02 11:32:03
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/LeetCode/95.不同的二叉搜索树-ii.py
'''
#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    # def build_tree(self,root,val):
    #     if root is None:
    #         root = TreeNode(val)
    #     else:
    #         if root.val < val:
    #             root.right = self.__build_tree(root.right,val)
    #         elif root.val > val:
    #             root.left = self.__build_tree(root.left,val)
    #     return root

        
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def buildTree(start,end):
            if start > end:
                return [None] #表示空树
                ## 不能空，否则左树和右树的循环不起作用
                ## 不能用两个None，元素会重复
                ## 一定要有返回[None],表示空树
            else start == end:
                return [TreeNode(start)] ## 表示只有根的树
            else:
                all_trees = []
                for i in range(start,end+1): # range 不包含下界
                    left_trees = buildTree(start,i-1)
                    right_trees = buildTree(i+1,end)
                    for lt in left_trees:
                        for rt in right_trees:
                            current_node = TreeNode(i)
                            current_node.right = rt
                            current_node.left = lt
                            all_trees.append(current_node)
                return all_trees
        trees = buildTree(1,n) if n > 0 else []
        return trees


                
# @lc code=end




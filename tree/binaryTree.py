'''
@Author: your name
@Date: 2020-06-29 15:38:52
@LastEditTime: 2020-06-29 17:48:09
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Algrithm/tree/binaryTree.py
'''
class TreeNode(object):
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class BST(object):
    def __init__(self,root=None):
        self.root = root

    def __add(self,root,val):
        if root is None:
            root = TreeNode(val)
        else:
            if val < root.val:
                root.left = self.__add(root.left,val)
            elif val > root.val:
                root.right = self.__add(root.right,val)
        return root

    def add(self,val):
        self.root = self.__add(self.root,val)

    def __isexist(self,root,val):
        if root is None:
            return False
        if root.val == val:
            return True
        elif root.val < val:
            return self.__isexist(root.right,val)
        elif root.val > val:
            return self.__isexist(root.left,val)

    def isexist(self,val):
        return self.__isexist(self.root,val)


    def __findMax(self,root):
        if root.right is None:
            return root
        else:
            return self.__findMax(root.right)

    def findMax(self):
        return self.__findMax(self.root)

    def __findMin(self,root):
        if root.left is None:
            return root
        else:
            return self.__findMin(root,left)

    def finMin(self):
        return self.__findMin(self.root)

    def __delete(self,root,val):
        if root is None:
            return None
            
        elif root.val > val:
            root.left = self.__delete(root.left,val)

        elif root.val < val:
            root.right = self.__delete(root.right,val)
            
        else:
            if root.right and root.left:
                min_right_node = self.__findMin(root.right)
                root.val = min_right_node.val
                root.right = self.__delete(root.right,root.val)

            elif root.right == None and root.left == None:
                root = None
            
            elif root.right == None and root.left != None:
                root = root.left

            elif root.right != None and root.left == None:
                root = root.right
                

    


if __name__ == "__main__":
    test = [7,9,8,6]
    bst = BST()
    for i in test:
        bst.add(i)
    # print(bst)
    print(bst.isexist(1))

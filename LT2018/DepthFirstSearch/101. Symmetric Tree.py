#!/usr/bin/env python2
# coding:utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        list_left = []
        list_right = []
        def listTree(x,val_type):
            if x:
                if val_type == 1:
                    list_left.append(x.val)
                elif val_type ==2:
                    list_right.append(x.val)
            if x.left:
                listTree(x.left, 1)
            if x.right:
                listTree(x.right, 2)
        # listTree(root,0)
        # print(list_left)
        # print(list_right)
        # if list_right == list_left:
        #     return True
        # else:
        #     return False
        if root is None:
            return True
        def isMirror(x_l,x_r):
            if x_l==None and x_r==None:
                return True
            if x_l==None or x_r==None:
                return False
            else:
                if x_l.val != x_r.val:
                    return False
                else:
                    bool_out = isMirror(x_l.left,x_r.right)
                    bool_in = isMirror(x_l.right, x_r.left)
                    return bool_in and bool_out
        return isMirror(root.left,root.right)


if __name__ == '__main__':
    data_input = [1,2,2,3,4,4,3]
    # data_tn = TreeNode(data_input[0])
    # data_input.pop(0)
    # data_tn.left = TreeNode
    # print(len(data_input))

    def treefun(x):
        # print(len(x))
        root = TreeNode(x[0])
        front = 0
        i = 0
        list_node = [root]
        while i < len(x)-1:
            base_node = list_node[front]
            i += 1
            front += 1
            # print(i)
            base_node.left = TreeNode(x[i])
            list_node.append(base_node.left)

            i += 1
            # print(i)
            base_node.right = TreeNode(x[i])
            list_node.append(base_node.right)
        return root

    x_test = treefun(data_input)
    y_output = Solution()
    print(y_output.isSymmetric(x_test))

    # def printTree(x,level_i):
    #     if x:
    #         print('level: ',level_i)
    #         print(x.val)
    #     if x.left and x.right:
    #         printTree(x.left,level_i+1)
    #         printTree(x.right,level_i+1)
    #
    # printTree(x_test,0)


    # for i in data_input:


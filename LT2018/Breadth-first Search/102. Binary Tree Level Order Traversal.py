#!/usr/bin/env python2
# coding:utf-8

'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def helper(root,res):
            res.append(root.val)
            res.append(helper(root.left,res)+helper(root.right,res))
        res = []
        return helper(root,res)

if __name__ == '__main__':
    data_input = [1, 2, 3, 3, 4, 4, 3]

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
            base_node.left = TreeNode(x[i])
            list_node.append(base_node.left)

            i += 1
            base_node.right = TreeNode(x[i])
            list_node.append(base_node.right)
        return root

    x_test = treefun(data_input)
    y_output = Solution()
    print(Solution().levelOrder(x_test))

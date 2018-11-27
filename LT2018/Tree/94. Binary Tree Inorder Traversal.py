#!/usr/bin/env python2
# coding:utf-8

'''
Given a binary tree, return the inorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root.left.left:
            return self.inorderTraversal(root.left)
        if root.right

if __name__ == '__main__':
    dt_input = TreeNode(1)
    dt_input.right = TreeNode(2)
    dt_input.right.left = TreeNode(3)

    def visit_tree(tnd):
        if tnd:
            print(tnd.val)
            if tnd.left:
                visit_tree(tnd.left)
            if tnd.right:
                visit_tree(tnd.right)
    # visit_tree(dt_input)
    print(Solution.inorderTraversal(dt_input))

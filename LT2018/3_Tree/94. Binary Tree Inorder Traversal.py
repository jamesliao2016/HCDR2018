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
        def helper(root,res=[]):
            if root:
                helper(root.left,res)
                res.append(root.val)
                helper(root.right,res)
        res = []
        helper(root,res)
        return res

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
    print(Solution().inorderTraversal(dt_input))

'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

# 1 apr, 2019
        def helper(root,res = []):
            if root:
                helper(root.left,res)
                res.append(root.val)
                helper(root.right,res)
        res = []
        helper(root,res)
        return res

5 dec, 2018
        if root.left.left:
            return self.inorderTraversal(root.left)
        if root.right

'''
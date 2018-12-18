#!/usr/bin/env python2
# coding:utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        while inorder:
            idx = inorder.index(preorder.pop(0))
            res = TreeNode(inorder[idx])
            res.left = self.buildTree(preorder,inorder[:idx])
            res.right = self.buildTree(preorder,inorder[idx+1:])
            return res

if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    def visit_tree(tnd):
        if tnd:
            print(tnd.val)
            if tnd.left:
                visit_tree(tnd.left)
            if tnd.right:
                visit_tree(tnd.right)
    # visit_tree(dt_input)
    visit_tree(Solution().buildTree(preorder,inorder))

    '''
    Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
   
   # dec 17
   
           if inorder:
            idx = inorder.index(preorder.pop(0))
            node = TreeNode(inorder[idx])
            node.left = self.buildTree(preorder,inorder[:idx])
            node.right = self.buildTree(preorder,inorder[idx+1:])
            return node

    '''
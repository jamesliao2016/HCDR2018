#!/usr/bin/env python2
# coding:utf-8
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        def helper(root):
            if root:
                helper(root.left)
                res.append(root.val)
                helper(root.right)
        helper(root)
        return res[k-1]

if __name__ == '__main__':
    dt_input = TreeNode(3)
    dt_input.right = TreeNode(4)
    dt_input.left = TreeNode(1)
    dt_input.left.right = TreeNode(2)
    k=1
    print(Solution().kthSmallest(dt_input,k))

'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?


'''
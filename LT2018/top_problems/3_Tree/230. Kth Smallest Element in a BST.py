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
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            tmp = stack.pop()
            k -= 1
            if k == 0:
                return tmp.val
            if tmp.right:
                stack.append(tmp.right)



if __name__ == '__main__':
# eg1
#     dt_input = TreeNode(3)
#     dt_input.right = TreeNode(4)
#     dt_input.left = TreeNode(1)
#     dt_input.left.right = TreeNode(2)
#     k=1
# eg2
    dt_input = TreeNode(5)
    dt_input.right = TreeNode(6)
    dt_input.left = TreeNode(3)
    dt_input.left.right = TreeNode(4)
    dt_input.left.left = TreeNode(2)
    dt_input.left.left.left = TreeNode(1)
    k=3

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
What if the 5_BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? 
How would you optimize the kthSmallest routine?

# 3 july, 2019
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            tmp = stack.pop()
            k-=1
            if k<1:
                return tmp.val
            root = tmp.right


# 24 MAY, 2019
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            tmp = stack.pop()
            k -= 1
            if k < 1:
                return tmp.val
            root = tmp.right

# 7 may, 2019
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            k-=1
            root = stack.pop()
            if k<1:
                return root.val
            root = root.right

# 9 apr, 2019
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k-=1
            if k<1:
                return root.val
            else:
                root = root.right


# 8 apr, 2019
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k-=1
            if k<1:
                return root.val
            else:
                root = root.right

# 8 mar, 2019
        stack =[]
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k<1:
                return root.val
            else:
                root = root.right


# 4 Mar, 2019
        def helper(root,res=[]):
            if root:
                helper(root.left,res)
                res.append(root.val)
                helper(root.right,res)
        res = []
        helper(root,res)
        return res

# 1 mar, 2019
        def helper(root,res=[]):
            if root:
                helper(root.left,res)
                res.append(root.val)
                helper(root.right,res)
        res = []
        helper(root,res)
        return res[-k]


# 28 feb, 2019

        res = []
        def helper(root):
            if root:
                helper(root.left)
                res.append(root.val)
                helper(root.right)
        helper(root)
        return res[k-1]


# 4 Jan, 2019
        res = []
        def helper(root):
            if root:
                helper(root.left)
                res.append(root.val)
                helper(root.right)
        helper(root)
        return res[k-1]



'''

'''
################################
##### Benchmark ################
################################
'''

'''
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
'''
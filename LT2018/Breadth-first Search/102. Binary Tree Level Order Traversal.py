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
        res = []
        tmp = [root]
        while tmp and root:
            res.append([i.val for i in tmp])
            ir = [[i.left,i.right] for i in tmp]
            tmp = [leaf for i in ir for leaf in i if leaf]
        return res

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

'''
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

# 30 DEC
        res,tmp = [], [root]
        while root and tmp:
            res.append([i.val for i in tmp])
            lr = [[i.left,i.right] for i in tmp]
            tmp = [leaf for i in lr for leaf in i if leaf]
        return res


# 29 DEC
        res,tmp = [],[root]
        while root and tmp:
            res.append([i.val for i in tmp])
            lr = [[i.left,i.right] for i in tmp]
            tmp = [leaf  for lr_tmp in lr for leaf in lr_tmp  if leaf]
        return res


# 5 dec, 2018

        def helper(root,res):
            res.append(root.val)
            res.append(helper(root.left,res)+helper(root.right,res))
        res = []
        return helper(root,res)

'''
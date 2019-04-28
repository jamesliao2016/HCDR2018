#!/usr/bin/env python2
# coding:utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        tmp = [root]
        cnt = 0
        while tmp and root:
            if cnt % 2 == 0:
                tmp0 = [i.val for i in tmp]
            else:
                tmp0 = [i.val for i in tmp][::-1]
            res.append(tmp0)
            lr = [[i.left, i.right] for i in tmp]
            tmp = [i for leaf in lr for i in leaf if i]
            cnt+=1
        return res


if __name__ == '__main__':
    # data_input = [1, 2, 3, 3, 4, 4, 3]
    data_input = [3,9,20,'null','null',15,7]

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
            if x[i]!='null':
                base_node.left = TreeNode(x[i])
                list_node.append(base_node.left)

            i += 1
            if x[i]!='null':
                base_node.right = TreeNode(x[i])
                list_node.append(base_node.right)
        return root

    x_test = treefun(data_input)
    y_output = Solution()
    print(Solution().zigzagLevelOrder(x_test))
'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

# 28 APR, 2019
        res,tmp = [],[root]
        cnt=0
        while tmp and root:
            if cnt%2==0:
                res.append([i.val for i in tmp])
            else:
                res.append([i.val for i in tmp][::-1])
            cnt += 1
            ir = [[i.left,i.right] for i in tmp]
            tmp = [leaf for i in ir for leaf in i if leaf]
        return res

# 12 dec

        res,tmp = [],[root]
        cnt = 0
        while root and tmp:
            if cnt%2==0:
                res.append([i.val for i in tmp])
            else:
                res.append([i.val for i in tmp][::-1])
            ir = [[i.left,i.right] for i in tmp]
            tmp = [leaf for i in ir for leaf in i if leaf]
        return res
        
'''
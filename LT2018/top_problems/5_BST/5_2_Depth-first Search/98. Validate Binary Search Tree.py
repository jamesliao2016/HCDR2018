#!/usr/bin/env python2
# coding:utf-8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root, smallerThan=float('inf'), largerThan=float('-inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.val <= largerThan or root.val >= smallerThan:
            return False
        else:
            return self.isValidBST(root.left,root.val,largerThan) and \
        self.isValidBST(root.right,smallerThan,root.val)

if __name__ == '__main__':
    # data_input = [1,2,2,3,4,4,3]
    data_input = [1, 2, 3, 3, 4, 4, 3]
    # data_input = [2,1,3]
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

    def visit_tree(tnd):
        if tnd:
            print(tnd.val)
            if tnd.left:
                visit_tree(tnd.left)
            if tnd.right:
                visit_tree(tnd.right)

    x_test = treefun(data_input)
    visit_tree(x_test)
    y_output = Solution()
    print(y_output.isValidBST(x_test))


    '''
    Given a binary tree, determine if it is a valid binary search tree (5_BST).

Assume a 5_BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
             
             # dec 29
             
        if not root:
            return True
        if root.val >= smallerThan or root.val <= largerThan:
            return False
        else:
            return self.isValidBST(root.left,root.val,largerThan)\
                   and self.isValidBST(root.right,smallerThan,root.val)
             
    '''
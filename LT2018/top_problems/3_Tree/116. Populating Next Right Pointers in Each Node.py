#!/usr/bin/env python2
# coding:utf-8

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root and root.left:
            nxt = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = nxt

if __name__ == '__main__':

    '''
    Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, 
the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, 
and every parent has two children).
Example:

Given the following perfect binary tree,

     1
   /  \
  2    3
 / \  / \
4  5  6  7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL

# 23 may, 2019
        while root and root.left:
            nxt = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = nxt

    '''


    '''
    
在这个recursion chapter学习自己悟出来的一个方法。
从example可以发现给的规律就是
每个节点（非叶子结点）必有两个子节点
对每一level的节点都进行如下操作
left.next = right
right.next = None
但是这里只是连接了两个节点，一层level里面节点不止这么多，还有中间的，就是左子树和右子树的之间的左子树的右节点，和右子树的左节点要连接起来，所以递归写了中间的
connect(left.right,right,left)
虽然最后实现了程序，但是改进的地方还是有序多
就比如，这个right.next = None，这里操作了多次，如果可以只要连接一次就连上的话是最好的了。

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        root.next = None
        def connect(left,right):
            if left and right:
                left.next = right
                right.next = None
                connect(left.left,left.right)
                connect(left.right,right.left)
                connect(right.left,right.right)
        connect(root.left,root.right)
        return root
很明显这个也可以用BFS来做，同样，也是之前从评论里面学到的queue实现的BFS来解决这里的问题

from collections import deque

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        root.next = None
        queue = deque([root])
        while queue:
            temp,size=[],len(queue)
            for i in range(size):
                node = queue.popleft()
                if node:
                    temp.append(node)
                if node.left and node.right:
                    queue.append(node.left)
                    queue.append(node.right)
            for index,node in enumerate(temp[:-1]):
                node.next = temp[index+1]
            temp[-1].next = None
        return root
从评论里面学到的一个方法，确实，BFS可以使用，但是我们没有必要用一个queue来存储node，
因为node有next节点，当我们有一个头结点之后，就可以像链表一样去访问了。
reference：
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37465/Python-Solution-With-Explaintion

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        cur = root
        nex = cur.left
        while cur.left:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = nex
                nex = cur.left
        return root    
    '''
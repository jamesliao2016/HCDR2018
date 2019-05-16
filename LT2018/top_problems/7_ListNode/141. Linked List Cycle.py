#!/usr/bin/env python2
# coding:utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        s,f = head,head.next
        while s and f:
            if s == f:
                return True
            if not s.next or not f.next:
                break
            s = s.next
            f = f.next.next
        return False



if __name__ == '__main__':
    l1=ListNode(3)
    l1.next = ListNode(2)
    l1.next.next = ListNode(0)
    l1.next.next.next = ListNode(-4)
    l1.next.next.next.next = l1.next
    print(Solution().hasCycle(l1))


'''
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, 
we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

 
Follow up:

Can you solve it using O(1) (i.e. constant) memory?

DEC 31
        try:
            slow,fast = head,head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

'''
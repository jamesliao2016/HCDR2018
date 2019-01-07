#!/usr/bin/env python2
# coding:utf-8
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res0 = odd = ListNode(0)
        res1 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            head = head.next.next if head.next else None
            odd = odd.next
            even = even.next
        odd.next = res1.next
        return res0.next

if __name__ == '__main__':
    l1=ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    zz = Solution().oddEvenList(l1)
    # zz=l1
    while zz:
        print(zz.val)
        zz=zz.next

'''
Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

# 7 jan, 2019
        res0 = odd = ListNode(0)
        res1 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            head.next = head.next.next if head.next else None
            head = head.next
            odd = odd.next
            even = even.next
        odd.next = res1.next
        return res0.next

'''
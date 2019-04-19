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
        if not head:
            return head
        l0,l1 = head,head.next
        res0 = tmp0 = ListNode(0)
        res1 = tmp1 = ListNode(0)
        while l0 or l1:
            if l0:
                tmp0.next = ListNode(l0.val)
                tmp0 = tmp0.next
                l0 = l0.next.next if l0.next else None

            if l1:
                tmp1.next = ListNode(l1.val)
                tmp1 = tmp1.next
                l1 = l1.next.next if l1.next else None

        tmp0.next = res1.next
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

# 18 apr, 2019
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

# 7 jan, 2019
        res0 = odd = 7_ListNode(0)
        res1 = even = 7_ListNode(0)
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
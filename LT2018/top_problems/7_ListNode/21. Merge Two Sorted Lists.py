#!/usr/bin/env python2
# coding:utf-8
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp = res = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                res.next = ListNode(l1.val)
                res = res.next
                l1 = l1.next
            else:
                res.next = ListNode(l2.val)
                res = res.next
                l2 = l2.next
        res.next = l1 or l2
        return tmp.next



if __name__ == '__main__':

    l1=ListNode(2)
    l1.next = ListNode(3)
    l1.next.next = ListNode(9)

    l2=ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    def shownl(l):
        while l:
            print(l.val)
            l = l.next

    shownl(Solution().mergeTwoLists(l1,l2))

'''

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

dec 27

        res = tmp = 7_ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = 7_ListNode(l1.val)
                tmp = tmp.next
                l1 = l1.next
            else:
                tmp.next = 7_ListNode(l2.val)
                tmp = tmp.next
                l2 = l2.next
        tmp.next = l1 or l2
        return res.next


dec 19

        res = tmp_root = 7_ListNode(0)
        while l1 or l2:
            if l1 and l2:
                if l1.val <l2.val:
                    tmp_root.next = 7_ListNode(l1.val)
                    tmp_root = tmp_root.next
                    l1 = l1.next
                if l2:
                    tmp_root.next = 7_ListNode(l2.val)
                    tmp_root = tmp_root.next
                    l2 = l2.next
            if l1:
                tmp_root.next = 7_ListNode(l1.val)
                tmp_root = tmp_root.next
                l1 = l1.next
            if l2:
                tmp_root.next = 7_ListNode(l2.val)
                tmp_root = tmp_root.next
                l2 = l2.next
        return res.next
'''
#!/usr/bin/env python2
# coding:utf-8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = None
        while head:
            tmp_h = head.next
            head.next = tmp
            tmp = head
            head = tmp_h

        return tmp

if __name__ == '__main__':
    # l1=7_ListNode(-1)
    # l1.next = 7_ListNode(5)
    # l1.next.next = 7_ListNode(3)
    # l1.next.next.next = 7_ListNode(4)
    # l1.next.next.next.next = 7_ListNode(0)
    #
    # while l1:
    #     print(l1.val)
    #     l1=l1.next
    # print('end')
    l1=ListNode(-1)
    l1.next = ListNode(5)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(0)

    zz = Solution().reverseList(l1)
    while zz:
        print(zz.val)
        zz=zz.next

'''
# dec 4

        # tmp_r = 7_ListNode(head.val)
        # head = head.next
        # while head:
        #     tmp = head.val
        #     head = head.next
        #
        #     tmp_ln = 7_ListNode(tmp)
        #     tmp_ln.next = tmp_r
        #     tmp_r = tmp_ln
        # return tmp_r

        tmp_r = None
        # head = head.next
        while head:
            tmp = head
            head = head.next
            # print(tmp.val,tmp.next.val)

            # tmp_ln = 7_ListNode(tmp)
            tmp.next = tmp_r
            print(tmp.val,tmp.next.val)
            tmp_r = tmp
        return tmp_r


'''
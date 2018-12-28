class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = tmp = head
        for _ in range(n):
            tmp = tmp.next
        if not tmp:
            return head
        while tmp.next:
            tmp = tmp.next
            slow = slow.next
        slow.next = slow.next.next
        return head

if __name__ == '__main__':

    l1=ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    #
    #
    # while l1:
    #     print(l1.val)
    #     l1=l1.next
    # tmp = l1

    zz = Solution()
    zz = zz.removeNthFromEnd(l1,2)

    while zz:
        print(zz.val)
        zz=zz.next
    # while tmp:
    #     print(tmp.val)
    #     tmp=tmp.next

    '''
    Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

DEC 26

        tmp = slow = head
        for _ in range(n):
            tmp = tmp.next
        if not tmp:
            return head
        while tmp.next:
            tmp = tmp.next
            slow = slow.next
        slow.next = slow.next.next
        # tmp = tmp.next
        # slow = slow.next
        # slow.next = slow.next.next
        # return slow
        # return tmp
        return head

DEC 25
    
            # res = ListNode(head.val)
        # head = head.next
        tmp = slow = head

        for _ in range(n):
            tmp = tmp.next

        if not tmp:
            return head.next
        while tmp.next:
            tmp =  tmp.next
            slow = slow.next
        slow.next = slow.next.next
        # slow.next.next = slow.next.next.next
        # tmp.next.next = tmp.next.next.next

        return head

    '''
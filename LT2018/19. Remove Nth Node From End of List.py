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
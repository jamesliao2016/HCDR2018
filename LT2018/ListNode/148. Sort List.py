class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def mg(l,r):
            res = tmp = ListNode(0)
            while l and r:
                if l.val > r.val:
                    tmp.next = ListNode(r.val)
                    tmp = tmp.next
                    r = r.next
                else:
                    tmp.next = ListNode(l.val)
                    tmp = tmp.next
                    l = l.next
            tmp.next = l or r
            return res.next
        if not head or not head.next:
            return head
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return mg(l,r)


if __name__ == '__main__':

    l1=ListNode(-1)
    l1.next = ListNode(5)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(0)
    #
    #
    # while l1:
    #     print(l1.val)
    #     l1=l1.next
    # tmp = l1

    zz = Solution()
    zz = zz.sortList(l1)
    #
    while zz:
        print(zz.val)
        zz=zz.next
    # while tmp:
    #     print(tmp.val)
    #     tmp=tmp.next

    '''
    Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

    '''
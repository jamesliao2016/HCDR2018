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
        def mergeList(l1,l2):
            res = tmp = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    tmp.next = ListNode(l1.val)
                    tmp = tmp.next
                    l1 = l1.next
                else:
                    tmp.next = ListNode(l2.val)
                    tmp = tmp.next
                    l2 = l2.next
            tmp.next = l1 or l2
            return res.next

        if not head or not head.next:
            return head

        s,f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        tail = s.next
        s.next = None
        head1 = self.sortList(head)
        tail1 = self.sortList(tail)
        return mergeList(head1,tail1)




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

# 16 may, 2019
        def merList(l1,l2):
            res = tmp = ListNode(0)
            while l1 and l2:
                if l1.val<l2.val:
                    tmp0 = l1.val
                    tmp.next = ListNode(tmp0)
                    tmp = tmp.next
                    l1 = l1.next
                else:
                    tmp0 = l2.val
                    tmp.next = ListNode(tmp0)
                    tmp = tmp.next
                    l2 = l2.next
            tmp.next = l1 or l2
            return res.next
        if not head or not head.next:
            return head
        s,f = head,head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        l2 = s.next
        s.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(l2)
        return merList(l1,l2)

# 25 apr, 2019
        def mergeList(l1,l2):
            res = tmp = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    tmp_val = l1.val
                    l1 = l1.next
                else:
                    tmp_val = l2.val
                    l2 = l2.next
                tmp.next = ListNode(tmp_val)
                tmp = tmp.next
            tmp.next = l1 or l2
            return res.next
        if not head or not head.next:
            return head
        f,s = head.next,head
        while f and f.next:
            s = s.next
            f = f.next.next
        tail = s.next
        s.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(tail)
        return mergeList(l1,l2)


# 10 apr, 2019

        def mergeList(l1,l2):
            res = tmp = ListNode(0)
            while l1 and l2:
                if l1.val<l2.val:
                    tmp.next = ListNode(l1.val)
                    tmp = tmp.next
                    l1 = l1.next
                else:
                    tmp.next = ListNode(l2.val)
                    tmp = tmp.next
                    l2 = l2.next
            tmp.next = l1 or l2
            return res.next
        if not head:
            return None
        if head:
            if not head.next:
                return head
            else:
                f,s = head.next,head
                while f and f.next:
                    s = s.next
                    f = f.next.next
                tail = s.next
                s.next = None
                l1 = self.sortList(head)
                l2 = self.sortList(tail)
                return mergeList(l1,l2)


# 9 apr, 2019
    def mergeLN(self,l1, l2):
        res = tmp = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tmp.next = ListNode(l2.val)
                l2 = l2.next
            tmp = tmp.next
        tmp.next = l1 or l2
        return res.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow,fast = head,head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tail = slow.next
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(tail)
        return self.mergeLN(l1,l2)

# 14 feb, 2019
        def mergeLN(l1,l2):
            res = tmp = 7_ListNode(0)
            while l1 and l2:
                if l1.val<l2.val:
                    tmp.next = 7_ListNode(l1.val)
                    l1 = l1.next
                else:
                    tmp.next = 7_ListNode(l2.val)
                    l2 = l2.next
                tmp = tmp.next
            tmp.next = l1 or l2
            return res.next
        if not head or not head.next:
            return head
        slow , fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tail = slow.next
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(tail)
        # l1 = head
        # l2 = tail
        return mergeLN(l1,l2)
        # return l2

# 13 feb, 2019
        def mergeList(l1,l2):
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
        if not head or not head.next:
            return head
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tail = slow.next
        slow.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(tail)
        return mergeList(l1,l2)

# dec 31

        def divideList(head):
            if not head or not head.next:
                return head
            tmp = slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            tail = slow.next
            slow.next = None
            head = tmp
            l1 = divideList(head)
            l2 = divideList(tail)
            return mergeList(l1,l2)

        def mergeList(l1,l2):
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

        return divideList(head)

# dec 30
        def mg(l,r):
            res = tmp = 7_ListNode(0)
            while l and r:
                if l.val > r.val:
                    tmp.next = 7_ListNode(r.val)
                    tmp = tmp.next
                    r = r.next
                else:
                    tmp.next = 7_ListNode(l.val)
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

    '''
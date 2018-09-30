class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = n = ListNode(0)
        val_ca = 0
        while l1 or l2 or val_ca:
            v1,v2 = 0,0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            # print(v1,v2)
            val_ca,val_tmp = divmod(v1+v2+val_ca,10)

            n.next = ListNode(val_tmp)
            n = n.next
        res = res.next
        return res



if __name__ == '__main__':

    l1=ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2=ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    #
    #
    # while l1:
    #     print(l1.val)
    #     l1=l1.next
    # tmp = l1

    zz = Solution()
    zz = zz.addTwoNumbers(l1,l2)

    while zz:
        print(zz.val)
        zz=zz.next
    # while tmp:
    #     print(tmp.val)
    #     tmp=tmp.next

    # res = n = ListNode(0)
    # v_carry = 0
    # while l1 or l2:
    #     v1, v2 = 0, 0
    #     if l1:
    #         v1 = l1.val
    #         l1 = l1.next
    #     if l2:
    #         v2 = l2.val
    #         l2 = l2.next
    #     v_carry, tmp = divmod(v1 + v2 + v_carry, 10)
    #     n.next = ListNode(tmp)
    #     n = n.next
    # return res

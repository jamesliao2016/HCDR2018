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
        res = tmp = ListNode(0)
        val = 0
        while l1 or l2 or val:
            v1,v2= 0,0
            if l1:
                v1 = l1.val
                l1= l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            val,v0 = divmod(v1+v2+val,10)
            tmp.next = ListNode(v0)
            tmp = tmp.next
        return res.next



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


'''

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

DEC 21
        res = tmp_root = 7_ListNode(0)
        tmp_ten = 0
        while l1 or l2 or tmp_ten:
            tmp_1,tmp_2 = 0,0
            if l1:
                tmp_1 = l1.val
                l1 = l1.next
            if l2:
                tmp_2 = l2.val
                l2 = l2.next
            tmp_ten,tmp_cur = divmod(tmp_ten+tmp_1+tmp_2,10)
            tmp_root.next = 7_ListNode(tmp_cur)
            tmp_root = tmp_root.next
        return res.next

    # res = n = 7_ListNode(0)
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
    #     n.next = 7_ListNode(tmp)
    #     n = n.next
    # return res

'''
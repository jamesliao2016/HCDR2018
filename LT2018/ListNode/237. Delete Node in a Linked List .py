class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """


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
    zz = zz.deleteNode(l1,5)
    #
    while zz:
        print(zz.val)
        zz=zz.next
    # while tmp:
    #     print(tmp.val)
    #     tmp=tmp.next
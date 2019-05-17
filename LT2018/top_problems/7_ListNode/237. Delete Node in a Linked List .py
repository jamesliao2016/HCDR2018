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
        node.val = node.next.val
        node.next = node.next.next


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

    '''
    Write a function to delete a node (except the tail) in a singly linked list, 
    given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:



 

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, 
the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, 
the linked list should become 4 -> 5 -> 9 after calling your function.
 

Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.

    '''
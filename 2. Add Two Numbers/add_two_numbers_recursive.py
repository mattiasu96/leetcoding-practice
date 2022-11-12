# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2, remainder=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sum_numbers = l1.val + l2.val + remainder
        remainder = sum_numbers // 10
        node_value = sum_numbers % 10

        ret = ListNode(node_value)

        if (l1.next != None or l2.next != None or remainder != 0):
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, remainder)

        return ret
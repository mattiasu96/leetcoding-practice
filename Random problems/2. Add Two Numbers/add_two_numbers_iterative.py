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

        l3 = None
        current_node = l3

        while l1 or l2 or remainder != 0:
            sum_numbers = (l1.val if l1 else 0) + (l2.val if l2 else 0) + remainder

            remainder = sum_numbers // 10
            node_value = sum_numbers % 10

            new_node = ListNode(node_value)

            if not l3:
                l3 = new_node
                current_node = new_node
            else:
                current_node.next = new_node
                current_node = new_node

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return l3

l1 = ListNode(10, next=ListNode(5))
l2 = ListNode(10, next=ListNode(5))

solution = Solution()
l3 = solution.addTwoNumbers(l1=l1,l2=l2)

print(l3)

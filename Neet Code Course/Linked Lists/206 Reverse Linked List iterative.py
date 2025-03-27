from typing import Optional

# This solution works, but it can't be greatly improved in verbosity (shorter code) and generalized.
# At the moment I'm considering a first exception, a step and then I iterate. I can embedd everything in the iteration
# without extra checks.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        scan_pointer = head.next
        forward_memory_pointer = head.next
        head.next = None

        while forward_memory_pointer:
            forward_memory_pointer = scan_pointer.next
            scan_pointer.next = head
            head = scan_pointer
            scan_pointer = forward_memory_pointer

        return head


my_list = ListNode(1, ListNode(2, ListNode(3, None)))
solution = Solution()
reversed_list = solution.reverseList(my_list)
print(reversed_list)

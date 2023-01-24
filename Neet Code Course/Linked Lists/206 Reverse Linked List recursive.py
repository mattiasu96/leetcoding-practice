from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            # If head is empty or has reached the list end
            if head is None or head.next is None:
                return head

            # Reverse the rest list
            rest = reverse(head.next)

            # Put first element at the end
            head.next.next = head
            head.next = None

            # Fix the header pointer
            return rest
        return reverse(head)



my_list = ListNode(1, ListNode(2, ListNode(3, None)))
solution = Solution()
reversed_list = solution.reverseList(my_list)
print(reversed_list)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(cur, prev):
            if cur is None:
                return prev

            next = cur.next
            cur.next = prev
            return reverse(next, cur)

        return reverse(head, None)


my_list = ListNode(1, ListNode(2, ListNode(3, None)))
solution = Solution()
reversed_list = solution.reverseList(my_list)
print(reversed_list)

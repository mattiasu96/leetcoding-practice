class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        list_output_head = None
        list_pointer = list_output_head

        if bool(list1 is None) ^ bool(list2 is None):
            return list1 if list1 else list2

        while list1 and list2:
            if list1.val <= list2.val:
                node = ListNode()
                node.val = list1.val
                if not list_output_head:
                    list_output_head = node
                    list_pointer = list_output_head
                else:
                    list_pointer.next_node = node
                    list_pointer = list_pointer.next_node
                list1 = list1.next_node
            else:
                node = ListNode()
                node.val = list2.val
                if not list_output_head:
                    list_output_head = node
                    list_pointer = list_output_head
                else:
                    list_pointer.next_node = node
                    list_pointer = list_pointer.next_node
                list2 = list2.next_node

        if list_pointer:
            list_pointer.next_node = list1 if list1 else list2

        return list_output_head


solution = Solution()
merged_list = solution.mergeTwoLists(ListNode(1, ListNode(1)), ListNode(3, ListNode(4)))
print(merged_list)

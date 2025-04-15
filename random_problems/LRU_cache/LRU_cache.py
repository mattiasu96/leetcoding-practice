class ListNode:
    def __init__(self, key, value, prev, next):
        self.key: int = key
        self.value: int = value
        self.prev: ListNode = prev
        self.next: ListNode = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.address_cache = {}
        self.queue_head = None
        self.queue_tail = None

    def _add_new_node(self, key: int, value: int):
        new_node = ListNode(key, value, None, self.queue_head) # Need to connect the nodes!
        self.queue_head = new_node
        if self.queue_tail is None:
            self.queue_tail = new_node

    def _update_priority_queue(self, key):  # O(n)
        curr = self.queue_head
        while curr.key != key:
            curr = curr.next

        if curr.prev:
            curr.prev.next = curr.next

        if curr.next:
            curr.next.prev = curr.prev

        curr.prev = None
        self.queue_head.prev = curr
        curr.next = self.queue_head
        self.queue_head = curr
    
    def _delete(self):
        del self.cache[self.queue_tail.key]
        self.queue_tail = self.queue_tail.prev
        self.queue_tail.next = None
        

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        self._update_priority_queue(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if len(self.cache.keys()) >= self.capacity:
            self._delete()
        self.cache[key] = value
        self._add_new_node(key, value)

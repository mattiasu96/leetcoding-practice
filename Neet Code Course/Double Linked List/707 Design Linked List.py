# TODO: Complete this, this is not working for real

class ListNode:

    def __init__(self, prev, nxt, val):
        self.prev = prev
        self.next = nxt
        self.val = val


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        self.cur = None

    def get(self, index: int) -> int:
        if index > self.length or index < 0:
            return -1
        self.cur = self.head
        for i in range(index):
            self.cur = self.cur.next
        value = self.cur.value
        self.cur = None
        return value

    # I wrote this function independently at the beginning, but I can easily express them as function of the generic one
    def addAtHead(self, val: int) -> None:
        return self.addAtIndex(index=0, val=val)

    # I wrote this function independently at the beginning, but I can easily express them as function of the generic one
    def addAtTail(self, val: int) -> None:
        return self.addAtIndex(index=self.length, val=val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length or index < 0:
            return None

        if index == 0:
            new_node = ListNode(prev=None, nxt=self.head, val=val)
            self.head = new_node # Cambiare la logica partendo dal presupposto che mi sposto subito sul nuovo nodo
            if self.length != 0:
                self.head.prev = new_node
            else:
                self.tail = self.head
            self.length += 1
            return None

        if index == self.length:
            new_node = ListNode(prev=self.tail, nxt=None, val=val)
            self.tail = new_node
            if self.length != 0:
                self.head.next = self.tail
            else:
                self.head = self.tail
            self.length += 1
            return None

        self.cur = self.head
        for i in range(index):
            self.cur = self.cur.next

        new_node = ListNode(prev=self.cur, nxt=self.cur.next, val=val)

        self.cur.prev.next = new_node
        self.cur.prev = new_node
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.length or index < 0:
            return None

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return None

        if index == self.length:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return None

        self.cur = self.head
        for i in range(index):
            self.cur = self.cur.next

        self.cur.prev.next = self.cur.next
        self.cur.next.prev = self.cur.prev
        self.length -= 1


obj = MyLinkedList()
param_1 = obj.get(1)
obj.addAtHead(1)
obj.addAtTail(1)
obj.addAtIndex(2,2)
obj.deleteAtIndex(1)


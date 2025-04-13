class Heap:
    def build_heap(self, array: list) -> list:
        min_heap = []
        for element in array:
            self.add(min_heap, element)
        return min_heap

    def add(self, min_heap: list, val: int):
        min_heap.append(val)

        i = len(min_heap) - 1

        while i > 1 and min_heap[i] < min_heap[i // 2]:
            temp = min_heap[i // 2]
            min_heap[i // 2] = min_heap[i]
            min_heap[i] = temp
            i = i // 2

        return min_heap

    def pop(self, min_heap: list):
        if len(min_heap) == 1:
            return None

        if len(min_heap) == 2:
            return min_heap.pop()

        head = min_heap[1]
        min_heap[1] = min_heap.pop()

        i = 1

        while 2 * i < len(min_heap):
            if (
                2 * i + 1 < len(min_heap)
                and min_heap[2 * i + 1] < min_heap[2 * i]
                and min_heap[i] > min_heap[2 * i + 1]
            ):
                temp = min_heap[i]
                min_heap[i] = min_heap[2 * i + 1]
                min_heap[2 * i + 1] = temp
                i = i * 2 + 1
            elif min_heap[i] > min_heap[2 * 1]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break

        return min_heap

from random_problems.LRU_cache.LRU_cache import ListNode, LRUCache


def test_LRU_cache_no_temporal_order():
    lru_cache = LRUCache(capacity=100)

    lru_cache = LRUCache(capacity=3)
    inputs = [(2, "ciao"), (3, "Come sta?")]

    for key, value in inputs:
        lru_cache.put(key, value)

    assert lru_cache.get(2) == "ciao"
    assert lru_cache.get(3) == "Come sta?"
    assert lru_cache.get(5) == -1


def test_LRU_cache_queue():
    lru_cache = LRUCache(capacity=3)
    inputs = [(2, "ciao"), (3, "Come sta?"), (4, "Bene"), (5, "e tu?")]

    for key, value in inputs:
        lru_cache.put(key, value)

    queue = lru_cache.queue_head

    index = len(inputs) - 1
    while queue is not None:
        assert queue.key == inputs[index][0] and queue.value == inputs[index][1]
        print(queue.key)
        print(queue.value)
        index -= 1
        queue = queue.next

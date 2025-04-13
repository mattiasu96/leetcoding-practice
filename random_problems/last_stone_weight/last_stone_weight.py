import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first_stone = heapq.heappop(stones)
            second_stone = heapq.heappop(stones)

            if first_stone < second_stone:
                residual_weight = first_stone - second_stone
                heapq.heappush(stones, residual_weight)
            elif second_stone < first_stone:
                residual_weight = second_stone - first_stone
                heapq.heappush(stones, residual_weight)

        stones.append(0)
        return abs(stones[0])

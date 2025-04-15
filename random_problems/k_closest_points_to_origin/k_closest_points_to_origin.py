import heapq
from math import sqrt


class Solution:
    def _calculate_distance(self, x_1, y_1, x_2, y_2):
        return sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        min_heap = [
            (self._calculate_distance(point[0], point[1], 0, 0), point)
            for point in points
        ]

        heapq.heapify(min_heap)
        res = []
        while k > 0:
            _, point = heapq.heappop(min_heap)
            res.append(point)
            k = k - 1

        return res


solution = Solution()

print(solution.kClosest([[1, 3], [-2, 2]], 1))

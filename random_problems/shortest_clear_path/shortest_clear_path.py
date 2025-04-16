from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))

        if grid[0][0] == 1:
            return -1

        lenght = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return lenght + 1

                neighbors = [
                    [0, 1],
                    [0, -1],
                    [1, 0],
                    [-1, 0],
                    [1, 1],
                    [1, -1],
                    [-1, 1],
                    [-1, -1],
                ]
                for dr, dc in neighbors:
                    if (
                        min(r + dr, c + dc) < 0
                        or r + dr == ROWS
                        or c + dc == COLS
                        or (r + dr, c + dc) in visit
                        or grid[r + dr][c + dc] == 1
                    ):
                        continue

                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))

            lenght = lenght + 1

        return -1

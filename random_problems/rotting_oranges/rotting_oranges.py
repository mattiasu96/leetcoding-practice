from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = deque()
        visited = set()
        empty_cells = set()
        ROWS, COLS = len(grid), len(grid[0])
        time_passed = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))

                if grid[r][c] == 0:
                    empty_cells.add((r, c))

        while len(queue) > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in neighbors:
                    if (
                        min(r + dr, c + dc) < 0
                        or r + dr == ROWS
                        or c + dc == COLS
                        or (r + dr, c + dc) in visited
                        or grid[r + dr][c + dc] == 0
                        or grid[r + dr][c + dc] == 2
                    ):
                        continue

                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))

                if grid[r][c] == 1:
                    grid[r][c] == 2

            if len(queue) > 0:
                time_passed = time_passed + 1

        if len(visited) + len(empty_cells) != ROWS * COLS:
            return -1

        return time_passed

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        cache = [[0] * COLS for i in range(ROWS)]

        def dfs(row, col):
            if row >= ROWS or col >= COLS or obstacleGrid[row][col] == 1:
                return 0

            if cache[row][col] > 0:
                return cache[row][col]

            if row == ROWS - 1 and col == COLS - 1:
                return 1

            cache[row][col] = dfs(row + 1, col) + dfs(row, col + 1)
            return cache[row][col]

        return dfs(0, 0)

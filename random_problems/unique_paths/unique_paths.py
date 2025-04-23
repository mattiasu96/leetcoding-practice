class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for i in range(m)]

        def dfs(row, col):
            if row >= m or col >= n:
                return 0

            if cache[row][col] > 0:
                return cache[row][col]

            if row == m - 1 and col == n - 1:
                return 1

            cache[row][col] = dfs(row + 1, col) + dfs(row, col + 1)
            return cache[row][col]

        return dfs(0, 0)

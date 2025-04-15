class Solution:
    def matrix_dfs(self, grid, row, col, visited_land: set):
        if (
            row < 0
            or row == len(grid)
            or col < 0
            or col == len(grid[0])
            or (row, col) in visited_land
            or grid[row][col] == 0
        ):
            return set()

        visited_land.add((row, col))

        visited_land.update(self.matrix_dfs(grid, row + 1, col, visited_land))
        visited_land.update(self.matrix_dfs(grid, row - 1, col, visited_land))
        visited_land.update(self.matrix_dfs(grid, row, col + 1, visited_land))
        visited_land.update(self.matrix_dfs(grid, row, col - 1, visited_land))

        return visited_land

    def numIslands(self, grid: list[list[str]]) -> int:
        visited_land = set()
        number_of_islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited_land:
                    number_of_islands += 1
                    self.matrix_dfs(grid, row, col, visited_land)

        return number_of_islands

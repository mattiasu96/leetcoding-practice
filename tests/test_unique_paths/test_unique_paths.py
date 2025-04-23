from random_problems.unique_paths.unique_paths_obstacles import Solution


def test_unique_paths():
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

    result = Solution().uniquePathsWithObstacles(grid)
    assert result == 2


def test_unique_paths_empty():
    grid = [[0, 0]]

    result = Solution().uniquePathsWithObstacles(grid)
    assert result == 0

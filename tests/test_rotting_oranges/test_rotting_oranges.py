from random_problems.rotting_oranges.rotting_oranges import Solution


def test_rotting_oranges():
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

    result = Solution().orangesRotting(grid)

    assert result == 4

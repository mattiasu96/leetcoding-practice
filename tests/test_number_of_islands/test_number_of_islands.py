from random_problems.number_of_islands.number_of_islands import Solution


def test_1_element_matrix():
    input_one_island = [[1]]
    input_no_island = [[0]]

    solution = Solution()

    one_island = solution.numIslands(input_one_island)
    no_island = solution.numIslands(input_no_island)

    assert one_island == 1
    assert no_island == 0


def test_4_elements_matrix():
    input_one_island = [[0, 0], [0, 1]]
    input_no_island = [[0, 0], [0, 0]]

    solution = Solution()

    one_island = solution.numIslands(input_one_island)
    no_island = solution.numIslands(input_no_island)

    assert one_island == 1
    assert no_island == 0

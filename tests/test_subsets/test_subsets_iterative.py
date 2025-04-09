from random_problems.subsets.subsets_iterative import Solution

def test_subsets_3_elements():
    array = [1,2,3]
    reference = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    result = Solution().subsets(array)

    assert result == reference


def test_subsets_0_elements():
    array = []
    reference = [[]]

    result = Solution().subsets(array)

    assert result == reference




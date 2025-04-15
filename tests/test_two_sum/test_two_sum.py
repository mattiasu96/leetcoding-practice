from random_problems.two_sum.two_sum_optimized import Solution


def test_sum_two():
    nums = [2, 7, 11, 15]
    target = 9

    result = Solution().twoSum(nums, target)

    assert result == [0, 1]


def test_sum_two_non_ordered():
    nums = [3, 2, 4]
    target = 6

    result = Solution().twoSum(nums, target)

    assert result == [1, 2]

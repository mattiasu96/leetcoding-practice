# Doing the C style approach, even though fixed size array does not exist in python, I need to use numpy

import numpy as np


class Solution:
    def getConcatenation(self, nums: list[int]) -> np.ndarray:
        new_array = np.zeros(2 * len(nums), dtype=int)

        for i in range(2 * len(nums)):
            index = i % len(nums)
            new_array[i] = nums[index]

        return new_array


test_array = [1, 2, 3, 4]
solution = Solution()
result = solution.getConcatenation(test_array)
print(result)

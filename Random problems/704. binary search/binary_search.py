import math

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low_index = 0
        high_index = len(nums) - 1

        while low_index != high_index:

            if nums[math.ceil(high_index/2)] == target:
                return math.ceil(high_index/2)

            if nums[math.ceil(high_index/2)] > target:
                high_index = math.floor(high_index/2)

            if nums[math.floor(high_index/2)] == target:
                return math.floor(high_index/2)

            if nums[math.floor(high_index / 2)] < target:
                low_index = math.ceil(high_index / 2)


        return -1






array = [-1,1,3,5,6]
solution = Solution()
print(solution.search(array, 6))

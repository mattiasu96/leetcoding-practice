class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return [nums[i % len(nums)] for i in range(2 * len(nums))]

# Even more pythonic
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums+nums


test_array = [1, 2, 3, 4]
solution = Solution()
result = solution.getConcatenation(test_array)
print(result)

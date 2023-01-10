class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        current_unique_value = nums[0]
        index_update = 0

        for iterate_index in range(len(nums)):
            if nums[iterate_index] != current_unique_value:
                index_update = index_update + 1
                nums[index_update] = nums[iterate_index]
                current_unique_value = nums[iterate_index]

        return index_update + 1


test = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solution = Solution()
result = solution.removeDuplicates(test)
print(result)

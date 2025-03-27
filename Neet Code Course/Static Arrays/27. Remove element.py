class Solution(object):
    def removeElement(self, nums, val) -> int:
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        sequential_remove_counter = 0

        for scan_index in range(len(nums)):
            if nums[scan_index] == val:
                sequential_remove_counter += 1

            if nums[scan_index] != val:
                nums[scan_index - sequential_remove_counter] = nums[scan_index]

        return len(nums) - sequential_remove_counter


test = [0, 0, 1, 1, 1, 2, 2, 1, 1, 2, 2]
solution = Solution()
result = solution.removeElement(test, 1)
print(result)

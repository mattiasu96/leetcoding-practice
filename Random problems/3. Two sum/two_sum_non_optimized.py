# https://leetcode.com/problems/two-sum/description/

# time complexity: O(n^2)
# memory: O(1)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        array_size = len(nums)

        for i in range(0, array_size):
            for j in range(i+1, array_size):
                if nums[i] + nums[j] == target:
                    indexes = (i, j)
                    return indexes

array = [3,2,4]
target = 6

solution = Solution()

indexes = solution.twoSum(array, target)
print(indexes)
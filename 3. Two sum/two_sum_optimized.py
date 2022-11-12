
# time complexity: O(n)
# memory: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {value:index for value, index in zip(nums, range(0, len(nums)))}

        for i in range(0, len(nums)):
            desired_number = target - nums[i]
            if desired_number in hashmap and hashmap[desired_number] != i:
                return i, hashmap[desired_number]


array = [2,5,5,11]
target = 10

solution = Solution()

indexes = solution.twoSum(array, target)
print(indexes)

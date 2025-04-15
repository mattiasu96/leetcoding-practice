# time complexity: O(n)
# memory: O(n)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}

        for index, num in enumerate(nums):
            hashmap[num] = index

        for index, num in enumerate(nums):
            candidate = target - num

            if candidate in hashmap.keys() and index != hashmap[candidate]:
                return [index, hashmap[candidate]]

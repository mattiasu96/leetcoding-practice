class Solution:
    def rob(self, nums: list[int]) -> int:
        cache = {}

        def dfs(i):
            if i > len(nums) - 1:
                return 0

            if i in cache:
                return cache[i]

            cache[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return cache[i]

        return dfs(0)

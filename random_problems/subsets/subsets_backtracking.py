class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        hashmap = {}

        def backtracking(nums):
            if not nums or tuple(nums) in hashmap.keys():
                return

            hashmap[tuple(nums)] = "1"

            for i in range(len(nums)):
                backtracking(nums[0:i] + nums[i + 1 :])

        backtracking(nums)

        return [[]] + [list(sublist) for sublist in list(hashmap.keys())]

    def subsets_backtracking(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        def dfs(i, nums):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

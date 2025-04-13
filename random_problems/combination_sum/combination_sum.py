class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        subset = []

        def dfs(i):
            if sum(subset) == target:
                res.append(subset.copy())
                return

            if i >= len(candidates) or sum(subset) > target:
                return

            subset.append(candidates[i])
            dfs(i)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

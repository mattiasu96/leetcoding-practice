class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets = [[]]
        for num in nums:
            subsets+= [s + [num] for s in subsets]
        return subsets
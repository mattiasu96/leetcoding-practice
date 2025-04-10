class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets = [[]]
        for num in nums:
            new_subsets = []
            for subset in subsets:
                new_subsets.append(subset + [num])
            # subsets.append(new_subsets) # this doesnt work, why?
            subsets += new_subsets
        return subsets
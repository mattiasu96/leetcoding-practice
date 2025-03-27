# this solution uses sorting on the letters and then compares the ordered strings.
# time complexity is O(nlogn) and space is O(n) (I need an extra variable to store the sorted stuff)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        return s == t


solution = Solution()
print(solution.isAnagram("cazzo", "cacca"))

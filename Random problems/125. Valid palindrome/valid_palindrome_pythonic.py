import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^0-9a-z]+', '', s.lower())
        return s == s[::-1]


solution = Solution()
print(solution.isPalindrome("ab_a"))

# This has complexity O(n) and memory O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = len(s) - 1
        j = 0
        alphanum = False
        while i > 0 and j < len(s):

            char_1 = s[i]
            char_2 = s[j]

            if s[i].isalnum() or s[j].isalnum():
                alphanum = True

            while (not s[i].isalnum() or s[i].isspace()) and i > 0:
                i -= 1
                char_1 = s[i]

            if s[i].isupper():
                char_1 = s[i].lower()

            while (not s[j].isalnum() or s[j].isspace()) and j < len(s) - 1:
                j += 1
                char_2 = s[j]

            if s[j].isupper():
                char_2 = s[j].lower()

            if char_1 != char_2 and alphanum:
                return False

            i -= 1
            j += 1

        return True


solution = Solution()
print(solution.isPalindrome(",.."))

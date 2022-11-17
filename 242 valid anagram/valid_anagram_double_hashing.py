# this solution uses hashing (dictionary). If im not wrong, this should imply a O(N) time complexity and O(1) space
# The space occupied by the hashing in case of alphabetical char is always the same, independent from the input.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}
        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False

        for char_s, char_t in zip(s, t):
            if char_s not in hash_s:
                hash_s[char_s] = 1
            else:
                hash_s[char_s] += 1

            if char_t not in hash_t:
                hash_t[char_t] = 1
            else:
                hash_t[char_t] += 1

        return hash_s == hash_t


solution = Solution()
print(solution.isAnagram("cazzo", "cacca"))

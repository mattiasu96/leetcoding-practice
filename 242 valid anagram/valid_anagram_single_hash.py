class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = {}
        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False

        for char_s in s:
            if char_s not in hash_s:
                hash_s[char_s] = 1
            else:
                hash_s[char_s] += 1

        for char_t in t:
            if char_t not in hash_s:
                return False
            else:
                hash_s[char_t] -= 1

        for val in hash_s.values():
            if val != 0:
                return False

        return True


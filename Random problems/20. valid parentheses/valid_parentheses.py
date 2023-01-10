# decent solution, but can be greatly refactored

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 0 or len(s) == 1:
            return False

        if (s[0] == ")") | (s[0] == "]") | (s[0] == "}"):
            return False

        hashmap_parentheses = {")": "(", "]": "[", "}": "{"}
        queue = []

        for i in range(len(s)):

            closing_condition = (s[i] == ")") | (s[i] == "]") | (s[i] == "}")
            opening_condition = (s[i] == "(") | (s[i] == "[") | (s[i] == "{")

            if opening_condition:
                queue.insert(0, s[i])

            if closing_condition and len(queue) == 0:
                return False

            if (closing_condition) and hashmap_parentheses[s[i]] != queue[0]:
                return False

            if closing_condition:
                queue = queue[1:]

        if len(queue) != 0:
            return False

        return True


solution = Solution()

print(solution.isValid("()()]"))

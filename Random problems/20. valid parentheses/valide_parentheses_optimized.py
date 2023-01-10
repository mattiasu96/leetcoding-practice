
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack, hashmap_parentheses = [], {")": "(", "]": "[", "}": "{"}

        for input_char in s:
            if input_char in hashmap_parentheses:
                if not (stack and stack.pop() == hashmap_parentheses[input_char]):
                    return False
            else:
                stack.append(input_char)
        return not stack



solution = Solution()

print(solution.isValid("()()"))

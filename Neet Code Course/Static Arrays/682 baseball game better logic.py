class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []

        for command in operations:

            if command == "+":
                record.append(record[-1] + record[-2])  # farlo pythonic
            elif command == "D":
                record.append(2 * record[-1])  # farlo pythonic
            elif command == "C":
                record.pop()
            else:
                record.append(int(command))
        return sum(record)


test = ["1", "2", "3", "+", "C", "D"]

solution = Solution()
result = solution.calPoints(test)
print(result)

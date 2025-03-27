class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []

        for command in operations:
            try:
                number = int(command)
                record.append(number)
            except:
                pass

            if command == "+":
                record.append(record[-1] + record[-2])  # farlo pythonic

            if command == "D":
                record.append(2 * record[-1])  # farlo pythonic

            if command == "C":
                record.pop()

        return sum(record)


test = ["1", "2", "3", "+", "C", "D"]

solution = Solution()
result = solution.calPoints(test)
print(result)

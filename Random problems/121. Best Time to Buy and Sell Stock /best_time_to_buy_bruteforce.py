# O(n^2) time
# O(1) memory
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0

        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]

        return max_profit

solution = Solution()
print(solution.maxProfit([1, 7]))


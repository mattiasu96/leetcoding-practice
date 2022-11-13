# O(n) time
# O(1) memory
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        buy = 0
        sell = 1

        for _ in range(len(prices)-1):
            if prices[sell] - prices[buy] < 0:
                buy = sell
                sell += 1
            else:
                if prices[sell] - prices[buy] > max_profit:
                    max_profit = prices[sell] - prices[buy]
                sell += 1

        return max_profit


solution = Solution()
print(solution.maxProfit([2,3,4, 1, 7, 9]))

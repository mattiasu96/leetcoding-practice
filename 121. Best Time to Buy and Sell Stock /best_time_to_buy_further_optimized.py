# O(n) time
# O(1) memory
# This solution does not improve O(n), but reduces the amount of checks and storing variables and has cleaner code
# The whole idea is to just focus on finding the current minimum in the array and then subtract everything that
# comes after. Also removing subtractions and use only a < b is better than a - b < 0

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        minimum = prices[0]

        for current_price in prices:
            if current_price < minimum:
                minimum = current_price
            if current_price - minimum > max_profit:
                max_profit = current_price - minimum

        return max_profit


solution = Solution()
print(solution.maxProfit([2, 3, 4, 1, 7, 9]))

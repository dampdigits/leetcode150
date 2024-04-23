class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x, max_profit = len(prices)-1, 0

        for i in range(len(prices)-2, -1, -1):
            profit = prices[x] - prices[i]

            if profit > max_profit: max_profit = profit
            elif profit < 0: x = i

        return max_profit

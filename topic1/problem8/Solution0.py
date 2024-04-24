class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = prices[0], 0

        for p in prices:
            if p > cost:
                profit += p - cost
            cost = p
        
        return profit

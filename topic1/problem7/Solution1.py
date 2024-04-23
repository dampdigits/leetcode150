class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, max_profit = inf, 0

        for p in prices:
            if p < cost: cost = p
            elif p - cost > max_profit:
                max_profit = p - cost
        
        return max_profit

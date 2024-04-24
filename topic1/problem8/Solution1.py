class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cp, sp = prices[0], prices[0]

        for p in prices:
            if p > sp:
                sp = p
            elif p < sp:
                profit += sp - cp
                cp, sp = p, p
        
        return profit + sp - cp

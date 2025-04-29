class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if prices == sorted(prices):
            return prices[-1] - prices[0]
        elif prices == sorted(prices, reverse=True):
            return 0
        else:
            for i in range(0,len(prices)-1):
                if prices[i] < prices[i+1]:
                    max_profit += prices[i+1] - prices[i]
            return max_profit
        
        
                    
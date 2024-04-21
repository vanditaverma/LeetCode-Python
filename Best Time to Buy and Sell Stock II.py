class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        else:
            max_profit =0
            for i in range(1,len(prices)):
                if prices[i]>prices[i-1]:
                    max_profit = max_profit+ prices[i] - prices[i-1]
            return max_profit
                    
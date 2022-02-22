class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        mini = prices[0]
        
        for i in prices:
            if i < mini:
                mini = i
                
            else:
                profit = i - mini
                if profit > max_profit:
                    max_profit = profit
                    
        return max_profit

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit=0
        buyprice=prices[0]
        for i in range(1,len(prices)):
            if buyprice>prices[i]:
                buyprice=prices[i]
            else:
                profit=prices[i] - buyprice
                max_profit=max(max_profit,profit)
        return max_profit

                
            
            
                

        
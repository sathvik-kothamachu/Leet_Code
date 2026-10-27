class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # max_profit=0
        # buyprice=prices[0]
        # for i in range(1,len(prices)):
        #     if buyprice>prices[i]:
        #         buyprice=prices[i]
        #     else:
        #         profit=prices[i] - buyprice
        #         max_profit=max(max_profit,profit)
        # return max_profit
        min_price=float("inf")
        max_profit=0
        n=len(prices)
        for i in range(0,n):
            min_price=min(min_price,prices[i])
            max_profit=max(max_profit,prices[i]-min_price)
        return max_profit

                
            
            
                

        
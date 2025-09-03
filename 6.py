#The cost of stock on each day is given in an array price[]. Each day you may decide to either buy or sell the stock i at price[i], you can even buy and sell the stock on the same day. Find the maximum profit that you can get.

class Solution:
    def maximumProfit(self,prices):
        n=len(prices)
        profit=0

        for i in range(1,n):
           if prices[i]>prices[i-1]:
               profit += prices[i]-prices[i-1]
        return profit 
    
solution = Solution()
print(solution.maximumProfit([100, 180, 260, 310, 40, 535, 695]))
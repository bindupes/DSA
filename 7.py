#Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

class Solution:
    def maximum(self,prices):
        min_price=prices[0]
        max_profit = 0
        n=len(prices)
        for price in prices:
            if price<min_price:
                min_price=price
            
            elif price-min_price > max_profit:
                max_profit = price - min_price

            
        return max_profit 
solution = Solution()
print(solution.maximum([7,10,1,3,6,9,2]))

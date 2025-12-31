# find on which index, which value gives most profit for user to buy and sell. Ex: prices=[1,0,-1,5,2] profit=6, buy_day : 2 , price=-1 , sell_day = 3 , price= 5
def max_profit(prices):
  max_profit=0
  min_price=prices[0]
  min_day=0
  buy_day=None
  sell_day=None

 for i in range(1,len(prices)):
   if prices[i]<min_price:
     min_price=prices[i]
     min_day=i

     profit=prices[i]-min_price
     if profit>max_profit:
       max_profit=prices[0]
       buy_day=min_day
       sell_day=i
return max_profit,buy_day,sell_day

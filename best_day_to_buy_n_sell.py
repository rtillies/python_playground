import ipdb

def max_profit(prices):
  l = 0
  r = 1
  max_profit = 0
  while (r < len(prices)):
    current_profit = prices[r] - prices[l]
    if current_profit > 0:
  	  max_profit = max(current_profit, max_profit)
    else:
  	  l = r
    r += 1
  return max_profit


print(max_profit([7,1,5,3,6,4]))
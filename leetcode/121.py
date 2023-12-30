#best time to buy and sell stock  
def maxProfit(prices): #return int
    profit = 0
    min = 100000
 
    for val in prices:
        if val-min > profit:
            profit = val - min
   
        elif val < min:
            min = val
       
    
    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))



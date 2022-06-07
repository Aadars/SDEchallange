def maximumProfit(prices):
    mini = prices[0]
    maxi = 0
    for i in range(len(prices)):
        if(mini>prices[i]):
            mini = prices[i]
        else:
            maxi = max(maxi,prices[i]-mini)
    return maxi



print(maximumProfit([98,101,66,72]))

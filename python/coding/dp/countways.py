def countWays(bills, amount):
    dp=[0]*(amount+1)
    for bill in bills:
        dp[bill]=1
    for i in range(amount+1):
        for bill in bills:
            if i-bill >0:
                dp[i]+=dp[i-bill]
    print(dp)
    return dp[amount]
bills=[10,20]
amount=30
print(countWays(bills,amount))
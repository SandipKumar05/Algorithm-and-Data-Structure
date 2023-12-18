# incorrect
def sol(coins,v):
    coins.sort()
    print(coins)
    ans=0
    for i in coins[::-1]:
        i,j=v//i,v%i
        ans+=i
        v=j
        if v==0:
            break
    return ans
coins = [9,6,5,1]; V = 11
print(sol(coins,V))
# above greedy approch not works here, ans=3+3 but it will give you ans=4+1+1
# Use dynamic programing
def solution(coins,v):
    dp=[float('inf') for i in range(v+1)]
    dp[0]=0
    for coin in coins:
        for i in range(coin,v+1):
            dp[i]=min(dp[i],1+dp[i-coin])
    return dp[v] if dp[v] != float('inf') else -1
print(solution(coins,V))
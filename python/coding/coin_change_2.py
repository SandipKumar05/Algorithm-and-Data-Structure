# https://www.geeksforgeeks.org/coin-change-dp-7/

def count(arr,n,sum):
    if sum == 0:
        return 1
    if sum < 0:
        return 0
    if n<=0:
        return 0
    return count(arr,n-1,sum) + count(arr,n, sum-arr[n-1])

def solution(arr, sum):
    n=len(arr)
    return count(arr,n,sum)

arr=[2,5,3,6]
sum=10
print(solution(arr,sum))
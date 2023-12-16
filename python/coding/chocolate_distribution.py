# https://www.geeksforgeeks.org/chocolate-distribution-problem/

def solution(arr,m):
    n=len(arr)
    arr.sort()
    print(arr)
    i=0;j=m-1
    answer=arr[n-1]-arr[0]
    while j<n:
        answer=min(answer,arr[j]-arr[i])
        i+=1;j+=1
    return answer
arr = [12, 4, 7, 9, 2, 23, 25, 41,
           30, 40, 28, 42, 30, 44, 48,
           43, 50]
m = 7  # Number of students
print(solution(arr,m))
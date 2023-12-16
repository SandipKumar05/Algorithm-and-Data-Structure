# https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/


## brute force approch
def max_index(arr):
    n=len(arr)
    max_index=0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] <= arr[j]:
                max_index=max(max_index,j-i)
    return max_index

def max_index_opt(arr):
    n=len(arr)
    l_min=[0]*n
    r_max=[0]*n
    l_min[0]=arr[0]; r_max[n-1]=arr[n-1]
    for i in range(1,n):
        l_min[i]=min(arr[i], l_min[i-1])
    for i in range(n-2,-1,-1):
        r_max[i]=max(arr[i],r_max[i+1])
    i=0;j=0
    max_index=-1
    print(l_min,r_max)
    while (j<n and i<n):
        if l_min[i] <= r_max[j]:
            max_index=max(max_index,j-i)
            j+=1
        else:
            i+=1
    return max_index


arr=[9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
print(max_index_opt(arr))
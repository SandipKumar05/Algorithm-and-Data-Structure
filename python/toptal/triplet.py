def find_triplet_optimized(A, B, C):
    B.sort()
    result = []
    
    for b in B:
        i, k = 0, len(C) - 1
        
        while i < len(A) and k >= 0:
            if A[i] <= b and b <= C[k]:
                result.append((A[i], b, C[k]))
                break
            elif A[i] >= b:
                i += 1
            else:
                k -= 1
    
    return result
def brute_force(a,b,c):
    ans=[]
    for i in a:
        for j in b:
            for k in c:
                # print(i,j,k)
                if i<=j and j<=k:
                    # print('sandip')
                    ans.append([i,j,k])
    return ans
# Example usage:
A = [1, 4, 5, 8, 10]
B = [6, 9, 15]
C = [2, 3, 6, 6]

result = find_triplet_optimized(A, B, C)
print(result)
result=brute_force(A,B,C)
print(result)

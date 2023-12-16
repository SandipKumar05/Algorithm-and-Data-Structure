# https://leetcode.com/problems/permutations/description/

def permutation(l,left,n):
    if left==n:
        ans.append(l[:])
    for i in range(left,n):
        l[left], l[i] = l[i], l[left]
        permutation(l,left+1,n)
        l[left], l[i] = l[i], l[left]

l=[1,2,3]
print(l[:])
global ans
ans=[]
print(permutation(l,1,3))
print(ans)
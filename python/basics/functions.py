# def test(x,y):
#     return x,y

# a,b=test(3,2)
# print(a,b)

# def getUniformIntegerCountInInterval(A: int, B: int) -> int:
#     count=0
#     temp = [1,2,3,4,5,6,7,8,9]
#     un=[]

#     for j in range(1,13):
#         for i in temp:
#             a = str(i)*j
#             b=int(a)
#             un.append(b)
#     print(un)
#     for i in un:
#         if i >=A and i<=B:
#             count+=1
#     return count

# print(getUniformIntegerCountInInterval(75,300))

# def getMinimumDeflatedDiscCount(N, R):
#   i=R[-1]
#   j=len(R)-2
#   count=0
#   while j>=0:
#     if i<=R[j]:
#         R[j]=i-1
#         count+=1
#     i=R[j]
#     j-=1
#   print(R)  
#   return count

# print(getMinimumDeflatedDiscCount(5,[2, 5, 3, 6, 5]))

def getMinCodeEntryTime(N, M, C):
  count=0
  j=1
  for i in C:
    a = abs(N-i)+j
    b = abs(i-j)
    count+=min(a,b)
  return count

print(getMinCodeEntryTime(10,4,[9, 4, 4, 8]))
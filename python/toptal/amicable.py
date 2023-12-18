def sumOfDiv(n):
    sum=1
    for i in range(2,n):
        if n%i ==0:
            sum+=i
    return sum

def amicalbe(N):
    amicalbe_pair=[]
    sum_of_div={}
    for j in range(2,N):
        i=sumOfDiv(j)
        sum_of_div[j]=i
        if i<N and i in sum_of_div and sum_of_div[i]==j and i!=j:
            amicalbe_pair.append([i,j])
    return amicalbe_pair

print(amicalbe(2000))
# print(sumOfDiv(284))
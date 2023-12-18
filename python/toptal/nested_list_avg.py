sum=0
count=0
def avg(l):
    sum=0
    count=0
    def summ(l):
        nonlocal sum,count
        for i in l:
            print(i)
            if isinstance(i,list):
                summ(i)
            else:
                sum=sum+i
                count=count+1
    summ(l)
    print(sum,count)
    return sum,count

l=[1,2,[3,[4]],5]
sum,count=avg(l)
print(sum,count)
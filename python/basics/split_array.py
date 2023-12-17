def isSplit(n):
    sum=0
    for i in n:
        sum+=i
    if sum%2 == 1:
        return False
    else:
        half=sum/2
        for i in n:
            half-=i
            if half == 0:
                return True
    return False

print(isSplit([1,2,3,4,5,5]))
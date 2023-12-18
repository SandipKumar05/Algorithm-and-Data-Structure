def fibo(n):
    a,b=0,1
    for i in range(2,n+1):
        a,b=b,a+b
    return b
print(fibo(6))

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
print(gcd(18,48))

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(4))

def is_prime(n):
    print(n**0.5)
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(is_prime(15))

# matrix multipication
def mat_multi(mat1,mat2):
    result=[[0 for i in range(len(mat2[0]))] for j in range(len(mat1))]
    print(result)
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j]+=mat1[i][k]*mat2[k][j]
    return result
mat1=[[1,1],[2,2],[3,3]]
mat2=[[1,1,1],[2,2,2]]
print(mat_multi(mat1,mat2))

def is_power_two(n):
    if n>0 and n & (n-1)==0:
        return True
    return False
print(is_power_two(4))

def count_set_bits(n):
    ans=0
    while n:
        ans += n & 1
        n >>=1
    return ans
print(count_set_bits(4))

def sqrt(n):
    if n < 2:
        return n
    left, right = 2, n//2
    while left <= right:
        mid=(left+right)//2
        temp=mid*mid
        if temp == n:
            return mid
        elif temp < n:
            left = mid+1
        else:
            right = mid-1
    return right
print(sqrt(16),sqrt(12))

def sec_to_string(n):
    w=60*60*24*7
    d=w/7; h=d/24; m=h/60
    ans=''
    weeks, rem=int(n//w), n%w
    days, rem=int(rem//d), rem%d
    hours, rem=int(rem//h), rem%h
    mins, rem=int(rem//m), rem%m
    if weeks > 0:
        ans+=f'{weeks}w'
    if days > 0:
        ans+=f'{days}d'
    if hours >0:
        ans+=f'{hours}h'
    if mins>0:
        ans+=f'{mins}m'
    if rem >0:
        ans+=f'{int(rem)}s'
    return ans
print(sec_to_string(123456))

# sort a dic by value
a={'a':2,'b':4,'c':1,'d':10}

print(dict(sorted(a.items(), key=lambda x:x[1])))
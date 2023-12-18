# array
a=[3,4,1,2,3]
print("unique",set(a))
print("max=",max(a),"min=",min(a),"sum=",sum(a))
print(sorted(a)) # returned a sorted list
print(list(reversed(a)))
for i, v in enumerate(a):
    print(i,v)

# zipped function 
a=['a','b','c','v']
b=[2,1,4,5]
res=zip(a,b)
for i,j in res:
    print(i,j)

# map function
a=[3,2,4,5]
res=map(lambda x:x*x,a)
print("map function",res)

# filter function
a=[3,2,4,5]
res=filter(lambda x: x*x > 14,a)
print("filter function",res)

# lambda function
l_fuc=lambda x:len(x)
a=['sandip','abc','hello world']
print(l_fuc(a))


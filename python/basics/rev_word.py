
def rev_word(s):
    words=s.split(' ')
    res = []
    for w in words:
        i=0
        j=len(w)-1
        w=list(w)
        while i<j:
            temp=w[i]
            w[i]=w[j]
            w[j]=temp
            i+=1
            j-=1
        res.append(''.join(w))
    return res

# result=" "
# print(' '.join(rev_word("sandip is fan or marvel")))

# uniq char
# def unique(s):
#     s1=set(s)
#     print(s1)
#     if len(s) == len(s1):
#         return True
#     return False

# print(unique("abbbc"))

s=[]
s.append("a")
s.append("b")
s.append("c")
print(s)
print(s.pop(0))
print(s)

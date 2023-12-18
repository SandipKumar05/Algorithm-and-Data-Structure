def split(s,c):
    count = s.count(c)
    if count % 3 != 0:
        return []
    t_c=count//3
    ans=0
    c_c=0
    for i in range(len(s)):
        if s[i]==c:
            c_c+=1
        if t_c == c_c:
            c2_c=0
            for j in range(i+1,len(s)):
                if s[j]==c:
                    c2_c+=1
                if c_c == t_c:
                    ans+=1
                    print(i,j)
    return ans
s="abaccadd"
print(split(s,'a'))
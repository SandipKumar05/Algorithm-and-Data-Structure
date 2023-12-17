def solution(exp):
    s=[]
    ans=0
    for c in exp:
        if c in '({[':
            s.append(c)
        elif c in ')}]':
            if len(s)==0:
                ans+=1
            else:
                top=s.pop()
                if (top=='(' and c!=')') or (top=='{' and c!='}') or (top=='[' and c!=']'):
                    ans+=1
    ans+=len(s)
    return ans
print(solution('((a + b) * (c - d)'))
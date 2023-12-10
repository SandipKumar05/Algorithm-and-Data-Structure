def reverse(s):
    n=len(s)
    result=""
    for i in range(n-1,-1,-1):
        result+=s[i]
    return result

print(reverse("sandip"))
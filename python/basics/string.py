# s="sandip"

# print(s[0])
# x = "hello world"
# s = x[0:3]
# print(s)
# s = x[:3]
# print(s)

# for i in range(len(s)):
#     print(s[:i])
# a=1
# b=str(a)*2
# c=int(b)
# print(c)

def check_palin(word):
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            return False
    return True
a="sanas"
b=a[::-1]
print(a[::-1])
print(check_palin(a))
if a==b:
    print("yes")


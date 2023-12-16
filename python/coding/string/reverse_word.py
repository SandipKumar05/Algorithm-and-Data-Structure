# https://www.geeksforgeeks.org/reverse-words-in-a-given-string/

def reverse_word(s):
    res = " ".join(s.split(" ")[::-1])
    return res
s="hello world"
print(reverse_word(s))
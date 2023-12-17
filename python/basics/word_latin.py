
x="Adam wants to go to the university"

words=x.split(" ")
vowel="aeiou"
result=[]
index=1
for word in words:
    last='a'*index
    if word[0].lower() in vowel:
        result.append(word+"ma"+last)
    else:
        result.append(word[1:]+"ma"+last)
    index+=1
print(str(result))
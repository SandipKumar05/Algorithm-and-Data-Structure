f1=open('data1.csv')
f2=open('data2.csv')
g=9.8
f1.readline()
f2.readline()
data={}
result={}
for line1 in f1.readlines():
    Dinosaur,Pedal,Feet_length=line1.split(',')
    data[Dinosaur]={}
    data[Dinosaur]['Pedal']=Pedal
    data[Dinosaur]['Feet_length']=Feet_length

for line2 in f2.readlines():
    Dinosaur,StrideLength,MaxAge=line2.split(',')
    if data[Dinosaur]['Pedal'] == "Bipedal":
        data[Dinosaur]['Speed']=((float(data[Dinosaur]['Feet_length'])*float(StrideLength))/2)*g
        result[Dinosaur]=data[Dinosaur]['Speed']

a=sorted(result.items(), key=lambda x:x[1], reverse=True)
print(a)

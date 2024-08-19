# Approach	            Efficiency	Memory Usage	Notes
# for line in f	More efficient	Lower	Uses buffering for faster line-by-line reading.
# for line in f.readline()	Less efficient	Potentially higher	Reads each line individually, 
# requiring more disk access.
import csv
def sorted_speed():
    g=9.8
    data = {}
    with open("data1.csv", 'r') as f1:
        f1.readline()
        for line in f1:
            name, pedal, length = line.split(",")
            name = name.strip()
            data[name]={}
            data[name]["pedal"]=pedal.strip()
            data[name]["length"]=length.strip()
    with open("data2.csv", 'r') as f2:
        f2.readline()
        for line in f2:
            name, stride, age = line.split(",")
            name = name.strip()
            feet_len = float(data[name]["length"])
            if data[name]["pedal"] == "Bipedal":
                pedal = 2
            else:
                pedal = 4
            data[name]["speed"] = ((feet_len*float(stride))/pedal)*g
    data = dict(sorted(data.items(), key=lambda x: x[1]["speed"]), reverse=True)
    print(data.keys())

def sorted_speed_2():
    d = {}
    with open("data1.csv",'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            name, pedal, feet_length = row['Dinosaur'], row['Pedal'], row['Feet_length']
            d[name] = {}
            d[name]['pedal'] = 2 if pedal == 'Bipedal' else 4
            d[name]['feet_length'] = float(feet_length)
    
    with open('data2.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            name, stride_length = row['Dinosaur'], row['StrideLength']
            d[name]['stride_length'] = float(stride_length)
            speed = (d[name]['feet_length']*d[name]['stride_length']/d[name]['pedal'])*(9.8)
            d[name]['speed']= speed
    
    d = dict(sorted(d.items(), key=lambda x:x[1]['speed'], reverse=True))
    for k,v in d.items():
        print(k,v['speed'])

sorted_speed_2()
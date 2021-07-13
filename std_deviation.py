import csv 
import math

with open("number.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

def mean(data):
    m=len(data)
    total=0
    for n in data:
        total+=int(n)
    mean=total/m
    return mean

squared_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    squared_list.append(a)

sum=0
for i in squared_list:
    sum+=i

result=sum/(len(data)-1)
standard_deviation=math.sqrt(result)
print(standard_deviation)
import csv
import math
import statistics

with open("numbers.csv", newline = "" )as f:
    r = csv.reader(f)
    file_data = list(r)
    
data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for c in data:
        total += int(c)
    mean = total/n
    return mean

square_list= []
for g in data:
    a = int(g)-mean(data)
    a = a**2
    square_list.append(a)
    
sum = 0
for h in square_list:
    sum += h
    
result = sum/( len(data)-1 )
k = math.sqrt(result)
print(f"\nThe standard deviation is {k} \n")


m = [30,750,200,24,53,84,933,876,345,54]
print(f"\nderived using predifined method {statistics.stdev(m)} \n")
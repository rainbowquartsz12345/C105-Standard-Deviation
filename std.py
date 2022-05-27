import csv
import math

with open("data.csv" , newline = "") as f:
    r = csv.reader(f)
    file_data = list(r)
data = file_data[0]

# finding mean
def mean( data ):
    n = len(data)
    total = 0
    for c in data:
        total += int(c)
    mean = total/n
    return mean

square_list = []
for s in data:
    a = int(s) - mean(data) 
    a = a**2
    square_list.append(a)

sum = 0
for f in square_list:
    sum += f
    
result = sum/ ( len(data)-1 )

std = math.sqrt(result)


print(f"\nThe standard deviation is {std}\n")

d = [ 60,61,65,63,98,99,90,95,91,96 ]
import statistics
print(f"\nDerived using predefined method : {  statistics.stdev( d ) }\n")

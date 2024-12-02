l = [5, 6, 7, 8, 9, 10, -3]

i = 0
s = 0
j = 0
low = pow(10, 9)  

while j < len(l) and l[j] != -1:  
    i += 1  
    s += l[j]  
    if l[j] < low: 
        low = l[j]
    j += 1  
    
count = i  
_sum = s  
_min = low  
mean = _sum / count  

print("Count =\n", count, "\nSum =\n", _sum, "\nMinimum =\n", _min, "\nMean =\n", mean)
# it looks like I learned how to use git today
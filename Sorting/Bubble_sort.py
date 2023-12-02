l = [7,4,6,34,95,24,96]

for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp

print(l) 
l = [56,8,23,11,65,22,9]

for i in range(1,len(l)):
    j = i-1
    temp = l[i]
    while(j>=0 and l[j]>temp):
        l[j+1] = l[j]
        j-=1
    l[j+1] = temp
print(l)
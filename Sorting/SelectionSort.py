l = [54,4,23,75,16,4,8,11,56]

for i in range(len(l)):
    min_index = i
    for j in range(i, len(l)):
        if l[j]<l[min_index]:
            min_index = j
    temp = l[i]
    l[i] = l[min_index]
    l[min_index] = temp

print(l)
def bubble(lst):
    for i in range(1,len(lst)):
        for j in range(len(lst)-i):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst

def selection(lst):
    for i in range(len(lst)):
        index=mini=999999
        for j in range(i,len(lst)):
            if lst[j]<mini:
                mini=lst[j]
                index=j
        if lst[i]>lst[index]:
            lst[i],lst[index]=lst[index],lst[i]
    return lst
print(selection([6,4,7,34,79,22,1]))


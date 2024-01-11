def bubblesort(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    return l

def selectionsort(l):
    for i in range(len(l)):
        minindex = i
        for j in range(i, len(l)):
            if l[j]<l[minindex]:
                minindex = j
        temp = l[i]
        l[i] = l[minindex]
        l[minindex] = temp
    return l

def insertionsort(l):
    for i in range(1, len(l)):
        j = i-1
        temp = l[i]
        while (j>=0 and l[j]>temp):
            l[j+1] = l[j]
            j -= 1
        l[j+1] = temp
    return l

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        left_half = mergeSort(left)
        right_half = mergeSort(right)
        return Merge(left_half, right_half)
    
def Merge(left, right):
    merge = []
    left_index, right_index = 0,0
    while(left_index<len(left) and right_index<len(right)):
        if left[left_index]<right[right_index]:
            merge.append(left[left_index])
            left_index+=1
        else:
            merge.append(right[right_index])
            right_index+=1
    merge.extend(left[left_index:])
    merge.extend(right[right_index:])
    return merge

l = [5,56,22,96,3,4,1]
print(mergeSort(l))
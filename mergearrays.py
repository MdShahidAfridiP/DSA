import array

def mergesort(arr1, arr2):
    i=0
    j=0
    merged = []
    while (i<len(arr1) or j<len(arr2)):
        if i<len(arr1) and arr1[i]<arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
    print(merged)

mergesort([1,3,5,7],[2,4,6,8,9,15]) #O(n)
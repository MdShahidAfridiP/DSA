def distribute(lst):
    total=1
    for i in range(1,len(lst)):
        if lst[i]>lst[i-1]:
            total+=2
        else:
            total+=1
        
    return total

'''cases=int(input())
lst=[]
for i in range(cases):
    n=int(input())
    lst=list(map(int,input().split()))[:n]
    total=1
    for i in range(1,len(lst)):
        if lst[i]>lst[i-1]:
            total+=2
        else:
            total+=1
    print(total) '''

def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]

        mergesort(l)
        mergesort(r)

        i=j=k=0

        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1

        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        
        while j<len(r):
            arr[k]=r[j]
            j+=1
            k+=1


# arr=[14,46,43,27,57,41,45,21,70]
# mergesort(arr)
# print(arr)

def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)

def quicksort(arr,low,high):
    if low<high:
        mid=partition(arr,low,high)
        quicksort(arr,low,mid-1)
        quicksort(arr,mid+1,high)

nlist = [14,46,43,27,57,41,45,21,70]
quicksort(nlist,0,len(nlist)-1)
print(nlist)
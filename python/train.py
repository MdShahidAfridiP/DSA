
def findPlatform(arr, dep, n):
    plat_needed = 0
    result = 1
    i = 1
    j = 0

    while (i < n and j < n):
        if arr[i] < dep[j]:
            plat_needed+= 1
            dep[j]=arr[i]+dep[j]
            i+= 1
            j+=1
        # Else decrement count 
        # of platforms needed 
        elif (arr[i] >= dep[j]): 
            
            if arr[i]>dep[j]:
                plat_needed+= 1
            j+= 1

        # Update result if needed 
        if (plat_needed > result): 
            result = plat_needed 
        
    return result 

# driver code 
lst=[]
for i in range(int(input())):
    lst.append(list(map(int,input().split())))

arr=[]
dep=[]
for l in lst:
    arr.append(l[0])
    dep.append(l[1]) 
n = len(arr) 

print(findPlatform(arr, dep, n)) 

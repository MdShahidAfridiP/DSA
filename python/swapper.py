'''def minimumSwaps(arr):
    count=0
    for i in range(len(arr)):
        val=arr.index(min(arr[i:]))
        if arr[i]>arr[val]:
            #print(arr[i],arr[val],arr[val],arr[i])
            arr[i],arr[val]=arr[val],arr[i]
            count+=1
    return count,arr
'''
def minimumSwaps(arr):
    numSwaps = 0
    i = 0
    while(i < len(arr)-1):

        if arr[i] != i+1:
            tmp = arr[i]
            arr[i], arr[tmp-1] = arr[tmp-1], arr[i]
            numSwaps += 1
        else:
            i += 1
    return numSwaps

#print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))

'''n=ord(input())
temp=n-65
i,j=temp*2//2,temp*2//2
for k in range(1,temp+1):
    val=65
    for l in range(1,temp*2+1):
        if l<i or l>j:
            print(' ',end=' ')
        else:
            print(chr(val),end=' ')
            val+=1
    i-=1
    j+=1
    print()'''

'''n=int(input())
l,m=n*2//2,n*2//2
for i in range(1,n*2+1):
    for j in range(1,n*2+1):
        if j<l or j>m:
            print(' ',end=' ')
        elif j==l or j==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    if i>=n*2//2:
        l+=1
        m-=1
    else:
        l-=1
        m+=1
    print()'''

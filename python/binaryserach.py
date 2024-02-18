def insert():
    lst=[]
    n=int(input("enter the size of array : "))
    for i in range(n):
        lst.append(int(input("enter the value : ")))
    return lst

def search(beg,end,value,lst):
    if beg==end:
        if value==lst[beg]:
            print("value found at position : ",end="")
            return beg+1
        else:
            print("value not found!!! ")
            exit(0)
    mid=(beg+end)//2
    if value==lst[mid]:
        print("value found at position : ",end="")
        return mid+1
    elif value<lst[mid]:
        return search(beg,mid-1,value,lst)
    else:
        return search(mid+1,end,value,lst)

lst=insert()
while True:
    print(search(0,len(lst)-1,int(input("enter the value to search : ")),lst))
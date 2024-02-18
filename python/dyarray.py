def insert(lst,pos,val): #pass list pos value
    try:
        lst[pos]=val
        print(lst)
    except IndexError:
        lst+=[None]*len(lst)    #double the list if list index out of bound
        #print(lst)
        insert(lst,pos,val)     #recusrive call back to insert values

lst=[1,2]
for i in range(10):
    pos=int(input("enter the position :"))
    insert(lst,pos,int(input("enter the value :")))



class arrays:
    def __init__(self,size):
        self.array=[0]*size

    def insert(self,pos):
        if self.array[pos]==0:
            self.array[pos]=int(input("enter the value : "))
        else:
            print("already value existed")

    def traverse(self):
        for i in range(len(self.array)):
            print(self.array[i],end=" ")

    def delete(self,pos):
        if self.array[pos]!=0:
            self.array[pos]=0
        else:
            print("already empty...")

'''size=int(input("enter the size of array :"))
arr=arrays(size)
while(True):
    n=int(input("\n 1.insert 2.delete 3.traverse 4.exit \n enter your choice : "))
    if n==1:
        pos=int(input("enter the position to insert : "))
        arr.insert(pos)
    elif n==2:
        pos = int(input("enter the position to insert : "))
        arr.delete(pos)
    elif n==3:
        arr.traverse()
    elif n==4:
        exit(0)
    else:
        exit(0)'''

class tree:
    def __init__(self,size):
        self.index=None
        self.arr=[None]*size
        self.last=None

    def insert(self,value):
        if self.arr[1]==None:
            self.index=1
            self.arr[self.index]=value
            self.last=1
        else:
            if self.arr[2*self.index]==None:
                self.arr[2*self.index]=value
                self.last+=1
            elif self.arr[2*self.index+1]==None:
                self.arr[2*self.index+1]=value
                self.last+=1
                self.index+=1
            else:
                self.index+=1
    
    def preorder(self,pointer):
        if pointer>self.last:
            return
        else:
            print(self.arr[pointer])
            self.preorder(2*pointer)
            self.preorder(2*pointer+1)

    def delete(self,value):
        pointer=1
        while pointer<self.last:
            if self.arr[pointer]==value:
                self.arr[pointer]=self.arr.pop(self.last)
                self.arr[self.last]=None
            else:
                pointer+=1

obj=tree(int(input("enter the size : ")))
while True:
    n=int(input("1.insert 2.traverse 3.delete : "))
    if n==1:
        obj.insert(int(input("enter the value :")))
    elif n==2:
        obj.preorder(1)
    elif n==3:
        obj.delete(int(input("enter the value :")))
    else:
        exit(0)
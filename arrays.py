import array

class arrays:
    def __init__(self,n) -> None:
        self.arr = array.array('i', [0]*n)
    
    def push(self, num):
        self.arr = self.arr + array.array('i',[0])
        self.arr[len(self.arr)-1] = num

    def display(self):
        for i in range(len(self.arr)):
            print(self.arr[i], end=', ')
        print()
    
    def pop(self):
        print("pop element is ", self.arr[-1])
        self.arr = self.arr[:-1]
    
    def insert(self, num, pos):
        self.arr = self.arr + array.array('i',[0])
        for i in range(len(self.arr)-1, pos-1,-1):
            self.arr[i] = self.arr[i-1]
        self.arr[pos-1] = num
    
    def delete(self, pos):
        for i in range(pos-1, len(self.arr)-1):
            self.arr[i]=self.arr[i+1]
        self.arr = self.arr[:-1]
    
obj = arrays(int(input("enter the size of the Array : ")))
n=1
while(n):
    print("Enter your choice : ")
    n = int(input("1.PUSH 2.POP 3.INSERT 4.DELETE 5.DISPLAY 0.EXIT : "))
    if n==1:
        obj.push(int(input("enter the number : ")))
    elif n==2:
        obj.pop()
    elif n==3:
        obj.insert(int(input("Enter the number : ")), int(input("enter the position : ")))
    elif n==4:
        obj.delete(int(input("enter the position : ")))
    elif n==5:
        obj.display()
    else:
        n=0
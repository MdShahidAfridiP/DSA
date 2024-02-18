def fibo(n):
    if n<=2:
        return n-1
    else:
        return fibo(n-1)+fibo(n-2)

def odd_eve(n):
    if n==0:
        return
    else:
        odd_eve(n-1)
        if n%2==0:
            print("even : ",n)
        else:
            print("odd : ",n)

def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))

#n=int(input("enter the value : "))
#print(fibo(n))

class node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,val):
        if self.head==None:
            new=node(val)
            self.head=new
            self.tail=new
        else:
            new=node(val)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
            
    
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.value)
            temp=temp.next
    
    def reverse_trav(self):
        temp=self.tail
        while temp:
            print(temp.value)
            temp=temp.prev

    def delete(self):
        def begin(self):
            print(self.head.value," deleted")
            self.head=self.head.next
        def last(self):
            temp=self.head
            while temp.next.next:
                temp=temp.next
            print(temp.next.value,' deleted')
            temp.next=None
            self.tail=temp
        def between(self):
            pos=int(input("enter the position : "))
            temp=self.head
            for i in range(pos-1):
                temp=temp.next
            print(temp.next.value,' deleted')
            temp.next=temp.next.next
        choice=int(input('1.begin 2.last 3.position : '))
        if choice==1:
            begin(self)
        elif choice==2:
            last(self)
        else:
            between(self)

'''obj=LinkedList()
while True:
    n=int(input("1.insert 2.delete 3.traverse enter your choice : "))
    if n==1:
        obj.insert(int(input("enter the value : ")))
    elif n==2:
        obj.delete()
    elif n==3:
        obj.traverse()
    elif n==4:
        obj.reverse_trav()
    else:
        exit(0)'''

class bs:
    def __init__(self):
        self.root=None

    def write(self,root):
        root=100

    def read(self,root):
        print(root)

obj=bs()
obj.write(obj.root)
obj.read(obj.root)

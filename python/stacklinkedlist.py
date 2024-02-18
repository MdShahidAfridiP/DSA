class node:
    def __init__(self,value):
        self.data=value
        self.next=None


class Stackll:
    def __init__(self):
        self.head=-1

    def push(self):
        new=node(int(input("enter the value : ")))
        new.next=self.head
        self.head=new
        print("the element insert is : ",self.head.data)

    def pop(self):
        if self.head==-1:
            print("stack is empty..")
        else:
            print("the popped element is : ",self.head.data)
            self.head=self.head.next

    def peek(self):
        if self.head==-1:
            print("stack is empty..")
        else:
            print("element at top : ",self.head.data)


obj=Stackll()
while True:
    n=int(input("1.push 2.pop 3.peek 4.exit  : "))
    if n==1:
        obj.push()
    elif n==2:
        obj.pop()
    elif n==3:
        obj.peek()
    else:
        exit(0)
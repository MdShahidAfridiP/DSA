class Stack:
    def __init__(self,size):
        self.top=-1
        self.stack=[-1]*size

    def push(self):
        if self.top==len(self.stack)-1:
            print("stack id full..")
        else:
            self.top+=1
            self.stack[self.top]=int(input("enter the value : "))

    def pop(self):
        if self.top==-1:
            print("stack is empty..")
        else:
            self.stack[self.top]=0
            self.top-=1

    def peek(self):
        if self.top==-1:
            print("stack is empty..")
        else:
            print(self.stack[self.top])


obj=Stack(int(input("enter the size of stack : ")))
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
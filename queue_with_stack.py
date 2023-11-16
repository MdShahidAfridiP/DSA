class queue:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []
    
    def enqueue(self, x):
        while(self.s1):
            self.s2.append(self.s1.pop())
        self.s2.append(x)

        while(self.s2):
            self.s1.append(self.s2.pop())
        print(self.s1)
    
    def dequeue(self):
        if self.s1:
            p = self.s1.pop()
            print("popped element is : ", p)
    
n=1
obj = queue()
while(n):
    print("1.Enqueue 2.Dequeue 3.Exit ")
    n = int(input("enter your choice : "))
    if n==1:
        obj.enqueue(int(input("enter the value : ")))
    elif n==2:
        obj.dequeue()
    else:
        n=0
    

class Queuenode:
    def __init__(self,size):
        self.queue=[None]*size
        self.head=0
        self.tail=0

    def enqueue(self):
        val=int(input("enter the value : "))
        if self.tail==len(self.queue):
            self.tail=0
            if self.queue[self.tail]==None:
                self.queue[self.tail]=val
                self.tail+=1
            else:
                print("queue is full..")
        else:
            if  self.queue[self.tail]==None:
                self.queue[self.tail]=val
                self.tail += 1
            else:
                print("queue is full..")

    def dequeue(self):
        if self.queue[self.head]==None:
            print("queue is empty..")
        else:
            self.queue[self.head]=None
            self.head += 1

    def peek(self):
        if self.queue[self.tail-1]!=None:
            print(self.queue[self.tail-1])
        else:
            print("queue is empty")
        print(self.queue)

size=int(input("enter the size of the queue : "))
obj=Queuenode(size)
while True:
    n=int(input("1.enqueue 2.dequeue 3.peek 4.exit  : "))
    if n==1:
        obj.enqueue()
    elif n==2:
        obj.dequeue()
    elif n==3:
        obj.peek()
    else:
        exit(0)

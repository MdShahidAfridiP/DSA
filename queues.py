class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.last:
            self.last.next = new_node
            self.last = new_node
            return
        self.first = new_node
        self.last = new_node
    
    def dequeue(self):
        currentnode = self.first
        if currentnode:
            print("The dequeued element is : ", currentnode.value)
            self.first = currentnode.next
            return
    
    def peek(self):
        if self.first:
            print("the first element is : ", self.first.value)
        return None
    
n=1
obj = Queue()
while(n):
    print("1.enqueue 2.dequeue 3.peek 4.Exit")
    n = int(input("enter the value : "))
    if n==1:
        obj.enqueue(int(input("enter the value : ")))
    elif n==2:
        obj.dequeue()
    elif n==3:
        obj.peek()
    else:
        n=0
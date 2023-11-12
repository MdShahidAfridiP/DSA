class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
    
    def push(self, value):
        new_node = Node(value)
        if self.top == None:
            self.top = new_node
            self.bottom = new_node
            return
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top.next:
            print("The popped element is : ", self.top.value)
            self.top = self.top.next
            return
        self.top = None
    
    def peek(self):
        if self.top:
            print("the top value is : ", self.top.value)
    
    def lookup(self, value):
        currentnode = self.top
        while currentnode:
            if currentnode.value == value:
                print(currentnode.value, end=" -> ")
                print("found the value")
                return
            print(currentnode.value, end=" -> ")
            currentnode = currentnode.next

n=1
obj = Stack()
while(n):
    print("1.Push 2.Pop 3.Peek 4.Lookup 5.Exit ")
    n = int(input("Enter the value :  "))
    if n==1:
        obj.push(int(input("Enter the value : ")))
    elif n==2:
        obj.pop()
    elif n==3:
        obj.peek()
    elif n==4:
        obj.lookup(int(input("Enter the value : ")))
    else:
        n=0

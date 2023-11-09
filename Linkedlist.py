class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def append(self,value):
        new_node = Node(value)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1
    
    def lookup(self, value):
        currentnode = self.head
        while(currentnode):
            if currentnode.value == value:
                print(currentnode.value)
                print("value found !")
                return
            else:
                print(currentnode.value, end=" -> ")
            currentnode = currentnode.next
        print()
    
    def insert(self, index, value):
        if index <= 0:
            self.prepend(value)
        elif index > self.size:
            self.append(value)
        else:
            new_node = Node(value)
            currentnode = self.head
            for i in range(index-2):
                currentnode = currentnode.next
            new_node.next = currentnode.next
            currentnode.next = new_node
    
    def delete(self, value):
        currentnode = self.head
        prevnode = None
        while(currentnode):
            if currentnode.value == value:
                if prevnode:
                    prevnode.next = currentnode.next
                    if currentnode.next == None:
                        self.tail = prevnode
                    return
                else:
                    self.head = self.head.next
                    return
            prevnode = currentnode
            currentnode = currentnode.next



obj = LinkedList()
n=1
while(n!=0):
    print("1.prepend 2.append 3.insert 4.lookup 5.Delete 6.Exit")
    n = int(input("enter the option : "))
    if n==1:
        obj.prepend(int(input("enter the value : ")))
    elif n==2:
        obj.append(int(input("enter the value : ")))
    elif n==3:
        obj.insert(int(input("enter the index : ")), int(input("enter the value : ")))
    elif n==4:
        obj.lookup(int(input("enter the value : ")))
    elif n==5:
        obj.delete(int(input("enter the value : ")))
    else:
        n=0
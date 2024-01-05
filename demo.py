class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            currentnode = self.head
            while currentnode.next:
                currentnode = currentnode.next
            currentnode.next = new_node
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
    
    def lookup(self, value):
        currentnode = self.head
        while currentnode:
            if currentnode.value == value:
                print("value found : ", value)
                return
            currentnode = currentnode.next
    
    def insert(self, pos, value):
        new_node = Node(value)
        currentnode = self.head
        prevnode = 0
        for i in range(pos-1):
            prevnode = currentnode
            currentnode = currentnode.next
        if prevnode:
            prevnode.next = new_node
            new_node.next = currentnode
        else:
            self.prepend(value)

    def iterate(self):
        currentnode = self.head
        while currentnode:
            print(currentnode.value, end=", ")
            currentnode = currentnode.next

    def delete(self, value):
        currentnode = self.head
        prevnode = 0
        while currentnode:
            if currentnode.value == value:
                if prevnode:
                    prevnode.next = currentnode.next
                    return
                elif not prevnode and self.head.next:
                    self.head = self.head.next
                else:
                    self.head = None
            prevnode = currentnode
            currentnode = currentnode.next

obj = LinkedList()
n=1
while(n!=0):
    print("1.prepend 2.append 3.insert 4.lookup 5.Delete 6.iterate 8.Exit")
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
    elif n==6:
        obj.iterate()
    else:
        n=0


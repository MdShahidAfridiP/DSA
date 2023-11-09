class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None
    
class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
        else:
            new_node = Node(value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1
    
    def prepend(self,value):
        if self.head:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        else:
            self.append(value)
    
    def insert(self, index, value):
        if index > self.size:
            self.append(value)
            return
        elif index <=1 :
            self.prepend(value)
            return
        currentnode = self.head
        for i in range(index-2):
            currentnode = currentnode.next
        new_node = Node(value)
        new_node.next = currentnode.next
        new_node.prev = currentnode
        if currentnode.next:
            currentnode.next.prev = new_node
        currentnode.next = new_node
        self.size += 1

    
    def lookup(self, value):
        currentnode = self.head
        while(currentnode):
            if currentnode.value == value:
                print(currentnode.value, end= " -> ")
                print("found the value!")
                return
            else:
                print(currentnode.value, end= " -> ")
            currentnode = currentnode.next
        print()

    def supersearch(self, value):
        head = self.head
        tail = self.tail
        while(head != tail or head.value == tail.value):
            if head.value == value and tail.value==value:
                print(head.value)
                print("found in center!")
                return
            elif head.value == value:
                print(head.value)
                print("value found in head!")
                return
            elif tail.value == value:
                print(tail.value)
                print("value found in tail")
                return
            else:
                print("head value : ", head.value)
                print("tail value : ", tail.value)
                tail = tail.prev
                head = head.next
    
    def delete(self, value):
        currentnode = self.head
        while currentnode:
            if currentnode.value == value:
                if currentnode == self.head:
                    if self.head.next:
                        self.head = self.head.next
                        self.head.prev = None
                        return
                elif currentnode == self.tail:
                    if self.tail.prev:
                        self.tail = self.tail.prev
                        self.tail.next = None
                        return
                else:
                    currentnode.prev.next = currentnode.next
                    currentnode.next.prev = currentnode.prev
                    return
            currentnode = currentnode.next
    
    def reverseprint(self):
        tail = self.tail
        while(tail):
            print(tail.value, end=" -> ")
            tail = tail.prev
        print()
    
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev
                    

obj = DoubleLinkedList()
n=1
while(n!=0):
    print("1.prepend 2.append 3.insert 4.lookup 5.SuperSearch 6.Delete 7.reverseprint 8.Exit")
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
        obj.supersearch(int(input("enter the value : ")))
    elif n==6:
        obj.delete(int(input("enter the value : ")))
    elif n==7:
        obj.reverseprint()
    else:
        n=0
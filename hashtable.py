class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.key = None

class HashTable:
    def __init__(self, size) -> None:
        self.capacity = size
        self.table = {}
        self.size = 0
    
    def _hash(self, value) -> int:
        return hash(value) % self.capacity
    
    def insert(self, value):
        hashkey = self._hash(value)
        new_node = Node(value)
        if not self.table.get(hashkey):
            self.table[hashkey] = new_node
            self.size+=1
        else:
            currentnode = self.table[hashkey]
            while(currentnode):
                if currentnode.value == value:
                    print("this key already exists!")
                    return
                currentnode = currentnode.next
            new_node.next = self.table[hashkey]
            self.table[hashkey] = new_node
            self.size+=1
    
    def delete(self, value):
        hashkey = self._hash(value)
        if self.table.get(hashkey):
            currentnode = self.table[hashkey]
            previousnode = 0
            while currentnode:
                if currentnode.value == value:
                    if previousnode:
                        previousnode.next = currentnode.next
                    else:
                        self.table[hashkey] = currentnode.next
                    self.size-=1
                    return
                previousnode = currentnode
                currentnode = currentnode.next


    def display(self, key):
        hashkey = self._hash(key)
        if self.table.get(hashkey):
            currentnode = self.table[hashkey]
            while currentnode:
                if currentnode.value == key:
                    print("found the key!")
                    print("the value is : ", currentnode.value)
                    return
                currentnode = currentnode.next
    
obj = HashTable(7)
n=1
while(n!=0):
    print("1.Insert 2.Delete 3.Display 4.Exit")
    n = int(input("enter the option : "))
    if n==1:
        obj.insert(int(input("enter the value : ")))
    elif n==2:
        obj.delete(int(input("enter the value : ")))
    elif n==3:
        obj.display(int(input("enter the value : ")))
    else:
        n=0




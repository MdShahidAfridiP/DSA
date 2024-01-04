class Node:
    def __init__(self, value) -> None:
        self.value = value 
        self.next = None
    
class HashTable:
    def __init__(self) -> None:
        self.size = 0
        self.table = {}
    
    def _hash(self, value):
        return hash(value) % 7
    
    def insert(self, value):
        hashkey = self._hash(value)
        new_node = Node(value)
        if not self.table.get(hashkey):
            self.table[hashkey] = new_node
        else:
            currentnode = self.table[hashkey]
            while(currentnode):
                if currentnode.value == value:
                    print("value found!")
                    return
                currentnode = currentnode.next
            new_node.next = self.table[hashkey]
            self.table[hashkey] = new_node
        self.size += 1
    
    def delete(self, value):
        hashkey = self._hash(value)
        if self.table.get(hashkey):
            previousnode = 0
            currentnode = self.table[hashkey]
            while(currentnode):
                if currentnode.value == value:
                    if previousnode:
                        previousnode.next = currentnode.next
                    else:
                        self.table[hashkey] = currentnode.next
                    self.size -= 1
                    return
                previousnode = currentnode
                currentnode = currentnode.next
    
    def search(self, value):
        hashkey = self._hash(value)
        if self.table.get(hashkey):
            currentnode = self.table[hashkey]
            while currentnode:
                if currentnode.value == value:
                    print("value found! : ", currentnode.value)
                else:
                    print("iterating.. : ", currentnode.value)
                currentnode = currentnode.next
    
    def display(self):
        for k,v in self.table.items():
            print(k, end=" : ")
            currentnode = v
            while(currentnode):
                print(currentnode.value, end=", ")
                currentnode = currentnode.next
            print()

obj = HashTable()
n=1
while(n!=0):
    print("1.Insert 2.Delete 3.Search 4.Display 5.Exit")
    n = int(input("enter the option : "))
    if n==1:
        obj.insert(int(input("enter the value : ")))
    elif n==2:
        obj.delete(int(input("enter the value : ")))
    elif n==3:
        obj.search(int(input("enter the value : ")))
    elif n==4:
        obj.display()
    else:
        n=0

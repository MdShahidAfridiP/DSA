import array

class Arrays:
    def __init__(self, num) -> None:
        self.arr = array.array('i',[0]*num)
    
    def push(self, num):
        self.arr = self.arr + array.array('i', [0])
        self.arr[len(self.arr)-1] = num
    
    def pop(self):
        print("popped element is : ", self.arr[-1])
        self.arr = self.arr[:-1]
    
    def insert(self, num, pos):
        self.arr = self.arr + array.array('i', [0])
        for i in range(len(self.arr)-1, pos-1, -1):
            self.arr[i] = self.arr[i-1]
        self.arr[pos-1] = num
    
    def display(self):
        for i in range(len(self.arr)):
            print(self.arr[i], end=',')
        print()
    
    def delete(self, pos):
        for i in range(pos-1, len(self.arr)-1):
            self.arr[i] = self.arr[i+1]
        self.arr = self.arr[:-1]

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Hashtable:
    def __init__(self) -> None:
        self.size = 0
        self.table = {}
    
    def _hash(self, key):
        return hash(key) % 7
    
    def insert(self, value):
        hashkey = self._hash(value)
        new_node = Node(value)

        if not self.table.get(hashkey):
            self.table[hashkey] = new_node
            self.size += 1
        else:
            current_node = self.table[hashkey]
            while(current_node):
                if current_node.value == value:
                    print("the value already exists")
                    return
                current_node = current_node.next
            new_node.next = self.table[hashkey]
            self.table[hashkey] = new_node
            self.size += 1

    def delete(self, value):
        hashkey = self._hash(value)
        if not self.table[hashkey]:
            print("key not found!")
        else:
            current_node = self.table[hashkey]
            previousnode = 0
            while(current_node):
                if current_node.value == value:
                    if previousnode:
                        previousnode.next = current_node.next
                    else:
                        self.table[hashkey] = current_node.next
                    self.size -= 1
                    return
                previousnode = current_node
                current_node = current_node.next
    
    def display(self, value):
        hashkey = self._hash(value)
        if self.table.get(hashkey):
            current_node = self.table[hashkey]
            while(current_node):
                print(current_node.value, end = ',')
                current_node = current_node.next
            print()

obj = Hashtable()
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
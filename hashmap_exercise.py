class Node:
    def __init__(self, key) -> None:
        self.value = key
        self.next = None

class HashTable:
    def __init__(self) -> None:
        self.table = {}
        self.size = 0
    
    def _hash(self,key):
        return hash(key)
    
    def insert(self, key):
        new_node = Node(key)
        hashkey = self._hash(key)
        if self.table.get(hashkey):
            currentnode = self.table[hashkey]
            while(currentnode):
                if currentnode.value == key:
                    print("the value is recurring : ", key)
                    return 0
                currentnode = currentnode.next
            new_node.next = self.table[hashkey]
            self.table[hashkey] = new_node
            return 1
        self.table[hashkey] = new_node
        return 1

obj = HashTable()
n=1
while(n):
    key = int(input("enter the value : "))
    n = obj.insert(key)
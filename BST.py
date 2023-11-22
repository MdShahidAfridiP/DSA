class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
    
    def Insert(self, current, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return
        elif value < current.value:
            if not current.left:
                current.left = new_node
                return
            else:
                self.Insert(current.left, value)
        elif value > current.value:
            if not current.right:
                current.right = new_node
                return
            else:
                self.Insert(current.right, value)
    
    def Insert2(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return
        current = self.root
        while(True):
            if value < current.value:
                if not current.left:
                    current.left = new_node
                    return
                current = current.left
            elif value > current.value:
                if not current.right:
                    current.right = new_node
                    return
                current = current.right
    
    def search(self, current, value):
        if current.value == value:
            print(current.value, end = ' -> ')
            print("found the value!")
            return
        elif value < current.value and current.left:
            print(current.value, end = ' -> ')
            self.search(current.left, value)
        elif current.right:
            print(current.value, end = ' -> ')
            self.search(current.right, value)
    
    def search2(self, value):
        current = self.root
        while(current):
            if current.value == value:
                print(current.value, end=" -> ")
                print("found the value! ")
                return
            elif value < current.value:
                print(current.value, end=" -> ")
                current = current.left
            else:
                print(current.value, end=" -> ")
                current = current.right
        else:
            print("value not found!")
    
    def remove(self, root, key):
        if root == None:
            return
        if key < root.value:
            root.left = self.remove(root.left, key)
        elif key > root.value:
            root.right = self.remove(root.right, key)
        else:
            if root.left == None:
                return root.right
            
            elif root.right == None:
                return root.left
            else:
                succ=self.getsucc(root.right)
                root.data = succ
                root.right = self.remove(root.right, succ)
        return root

        #User function Template for pythone
    def getsucc(root):
        curr=root
        while(curr.left!=None):
            curr=curr.left
        return curr.data


n=1
obj = BST()
while(n):
    n = int(input("1.Insert 2.Search 3.Delete : "))
    if n==1:
        obj.Insert2(int(input("Enter the value : ")))
    elif n==2:
        obj.search2(int(input("Enter the value : ")))
    elif n==3:
        obj.remove(obj.root, int(input("Enter the value : ")))
    else:
        n=0

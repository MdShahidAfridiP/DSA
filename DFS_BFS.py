class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
class BST:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            current = self.root
            while(current):
                if value<current.value:
                    if current.left == None:
                        current.left = new_node
                        return
                    current = current.left
                elif value>current.value:
                    if current.right == None:
                        current.right = new_node
                        return
                    current = current.right
    
    def BFS(self):
        queue = [self.root]
        values = []
        while queue:
            node = queue.pop(0)
            values.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(values)
    
    def BFSR(self, queue, lists):
        if queue == []:
            return lists
        else:
            node = queue.pop(0)
            lists.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            return self.BFSR(queue, lists)
        
    def DFSInorder(self, current):
        if current:
            self.DFSInorder(current.left)
            print(current.value, end=" ")
            self.DFSInorder(current.right)
    
    def DFSpreporder(self, current):
        if current:
            print(current.value, end=" ")
            self.DFSpreporder(current.left)
            self.DFSpreporder(current.right)
    
    def DFSpostorder(self, current):
        if current:
            self.DFSpostorder(current.left)
            self.DFSpostorder(current.right)
            print(current.value, end=" ")

n=1
obj = BST()
while(n):
    n = int(input("1.Insert 2.BFS 3.BFSR 4.inorder 5.preorder 6.postorder : "))
    if n==1:
        obj.insert(int(input("enter the value : ")))
    elif n==2:
        obj.BFS()
    elif n==3:
        print(obj.BFSR([obj.root], []))
    elif n==4:
        obj.DFSInorder(obj.root)
    elif n==5:
        obj.DFSpreporder(obj.root)
    elif n==6:
        obj.DFSpostorder(obj.root)
    else:
        n=0

    
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
class BST:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            current_node = self.root
            while(True):
                if value < current_node.value:
                    if not current_node.left:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
                else:
                    if not current_node.right:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right

    def BFS(self):
        if self.root == None:
            return
        else:
            queue = [self.root]
            values = []
            while(queue):
                node = queue.pop(0)
                values.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        print(values)


n=1
obj = BST()
while(n):
    n = int(input("1.Insert 2.DFS : "))
    if n==1:
        obj.insert(int(input("enter the value : ")))
    elif n==2:
        obj.BFS()
    else:
        n=0
    
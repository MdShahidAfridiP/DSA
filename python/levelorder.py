class node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

class bst:
    def __init__(self):
        self.root=None

    def create(self):
        new=node(int(input("enter the value : ")))
        self.root=new

    def insert(self,root,value):
        if root!=None:
            if value>root.data:
                if root.right:
                    return self.insert(root.right,value)
                else:
                    new=node(value)
                    root.right=new
            else:
                if root.left:
                    return self.insert(root.left,value)
                else:
                    new=node(value)
                    root.left=new
        else:
            self.root=node(value)

    def bfs(self,root):
        queue=[]
        queue.append(root)
        while len(queue)>0:
            print(queue[0].data)
            node=queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def dfs(self,root):
        queue=[]
        queue.append(root)
        while len(queue)>0:
            node=queue.pop()
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

obj=bst()
while True:
    n=int(input("1.create 2.insert 3.levelorder  : "))
    if n==1:
        obj.create()
    elif n==2:
        obj.insert(obj.root,int(input("enter the value : ")))
    elif n==3:
        obj.bfs(obj.root)
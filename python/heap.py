class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class heap:
    def __init__(self):
        self.root=None
    
    def insert(self,root,value):
        if root==None:
            return node(value)
        elif value<=root.value:
            root.left=self.insert(root.left,value)
        elif value>root.value:
            root.right=self.insert(root.right,value)
        else:
            return root
        return root

    def inoroder(self,root):
        if root==None:
            return
        else:
            self.inoroder(root.left)
            print(root.value)
            self.inoroder(root.right)

    def search(self,root,value):
        if root==None:
            print("value not found..")
            return root
        elif value<root.value:
            root.left=self.search(root.left,value)
        elif value>root.value:
            root.right=self.search(root.right,value)
        elif value==root.value:
            print("value found...")
            return root
        else:
            return root
        return root
    
    def successor(self,root,lst=[]):
        if root==None:
            return None
        else:
            self.successor(root.left,lst)
            lst.append(root.value)
            self.successor(root.right,lst)
        return lst

    def delete(self,root,value):
        if root==None:
            return None
        elif value<root.value:
            root.left=self.delete(root.left,value)
        elif value>root.value:
            root.right=self.delete(root.right,value)
        else:
            if root.left==None and root.right==None:
                return None
            elif root.left and root.right:
                successor=self.successor(root.right).pop(0)
                root.value=successor
                root.right=self.delete(root.right,successor)
            else:
                root=root.left if root.left else root.right
        return root



obj=heap()
while True:
    n=int(input("1.insert 2.inorder 3.search 4.delete : "))
    if n==1:
        obj.root=obj.insert(obj.root,int(input("enter the value :")))
    elif n==2:
        obj.inoroder(obj.root)
    elif n==3:
        obj.search(obj.root,int(input("enter the value : ")))
    elif n==4:
        obj.delete(obj.root,int(input("enter the value : ")))
    else:
        exit(0)
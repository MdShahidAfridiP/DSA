class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class simpletree:
    def __init__(self):
        self.root=None
    
    def insert(self,value):
        if self.root==None:
            self.root=node(value)
        else:
            lst=[self.root]
            while len(lst):
                temp=lst.pop(0)
                if temp.left==None:
                    temp.left=node(value)
                    break
                else:
                    lst.append(temp.left)
                if temp.right==None:
                    temp.right=node(value)
                    break
                else:
                    lst.append(temp.right)
     
    def levelorder(self):
        lst=[self.root]
        while len(lst):
            temp=lst.pop(0)
            print(temp.value)
            if temp.left:
                lst.append(temp.left)
            if temp.right:
                lst.append(temp.right)

    def delete(self,value):
        lst=[self.root]
        while len(lst):
            temp=lst.pop(0)
            if temp.left:
                lst.append(temp.left)
            if temp.right:
                lst.append(temp.right)
        last=temp

        lst1=[self.root]
        while len(lst1):
            temp=lst1.pop(0)
            if temp.value==value:
                temp.value=last.value
            if temp.left==last:
                temp.left=None
            elif temp.right==last:
                temp.right=None
            if temp.left:
                lst1.append(temp.left)
            if temp.right:
                lst1.append(temp.right)
                
        

'''obj=simpletree()
while True:
    n=int(input("1.insert 2.levelorder 3.delete :"))
    if n==1:
        obj.insert(int(input("enter the value :")))
    elif n==2:
        obj.levelorder()
    elif n==3:
        obj.delete(int(input("enter the value to delete : "))) '''

class bstree:
    def __init__(self):
        self.root=None

    def insert(self,root,value):
        if root==None:
            root=node(value)
        else:
            if value<root.value:
                root.left=self.insert(root.left,value)
            elif value>root.value:
                root.right=self.insert(root.right,value)
        return root

    def preorder(self,root):
        if root==None:
            return
        else:
            print(root.value)
            self.preorder(root.left)
            self.preorder(root.right) 

    def successor(self,root,lst=[]):
        if root==None:
            return 
        else:
            self.successor(root.left,lst)
            lst.append(root.value)
            self.successor(root.right,lst)
        return lst

    def delete(self,root,value):
        if root==None:
            return root
        elif root.value<value:
            root.left=self.delete(root.left,value)
        elif root.value>value:
            root.right=self.delete(root.right,value)
        elif root.value==value:
            if root.left==None and root.right==None:
                return None
            elif root.left and root.right:
                successor=self.successor(root.right).pop(0)
                root.value=successor
                root.right=self.delete(root.right,successor)
            else:
                if root.left and root.right==None:
                    root=root.left
                elif root.right and root.left==None:
                    root=root.right
        return root

        

obj=bstree()
while True:
    n=int(input("1.insert 2.preorder 3.delete:"))
    if n==1:
        obj.root=obj.insert(obj.root,int(input("enter the value :")))
    if n==2:
        obj.preorder(obj.root)
    if n==3:
        obj.root=obj.delete(obj.root,int(input("enter the value : ")))
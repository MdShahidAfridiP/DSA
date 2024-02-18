'''while True:
    print("*************** main menu *****************")
    choice=int(input("1.create 2.insert 3.view 4.search \n enter your choice : "))
    if choice==1:
        val=int(input("enter the value : "))
        root = cnode(val)
        head=root
    if choice==2:
        def insert(node,value):
            if node.value:
                if value<node.value:
                    if node.left:
                        return insert(node.left,value)
                    else:
                        node.left=cnode(value)
                        print("value inserted at left")
                        return True
                else:
                    if node.right:
                        return insert(node.right,value)
                    else:
                        node.right=cnode(value)
                        print("value inserted at right")
                        return True
            else:
                node.value=value
                print("value inserted at root")
                return True
        value=int(input("enter the value : "))
        insert(root,value)

    if choice==3:
        print(f"head value is : {head.value}  \nleft child value is : {head.left.value}  \nright child value is : {head.right.value}")

    if choice==4:
        def search(node,value):
            if node.value==value:
                print("value has been found : ",node.value)
                return True
            elif value<node.value:
                return search(node.left,value)
            elif value>=node.value:
                return search(node.right,value)
            else:
                print("value not found sorry :( ")
                return False
        value=int(input("enter the value to search : "))
        search(root,value)

    else:
        pass '''

class node:
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None

class tree:
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
                    lst.append(temp.left)

    def delete(self,value):
        lst=[self.root]
        while len(lst):
            temp=lst.pop(0)
            if temp.left:
                lst.append(temp.left)
            if temp.right:
                lst.append(temp.right)
        lst2=[self.root]
        while len(lst2):
            temp1=lst2.pop(0)
            if temp1.left==temp:
                temp1.left=None
            elif temp1.right==temp:
                temp1.right=None
            if temp1.value==value:
                temp1.value=temp.value
            if temp1.left:
                lst2.append(temp1.left)
            if temp1.right:
                lst2.append(temp1.right)
        
    
    def preorder(self,root):
        if root==None:
            return
        else:
            print(root.value)
            self.preorder(root.left)
            self.preorder(root.right)

'''obj=tree()
while True:
    n=int(input("1.insert 2.traverse 3.delete : "))
    if n==1:
        obj.insert(int(input("enter the value : ")))
    elif n==2:
        obj.preorder(obj.root)
    elif n==3:
        obj.delete(int(input("enter the value : ")))
    else:
        exit(0)'''

class bst:
    def __init__(self):
        self.root=None

    def insert(self,root,value):
        if root==None:
            root=node(value)
        elif value<=root.value:
            root.left=self.insert(root.left,value)
        else:
            root.right=self.insert(root.right,value)
        return root

    def preorder(self,root,lst=[]):
        if root==None:
            return 
        else:
            self.preorder(root.left,lst)
            lst.append(root.value)
            self.preorder(root.right,lst)
        return lst

    def predecessor(self,root,lst=[]):
        if root==None:
            return
        else:
            self.predecessor(root.left,lst)
            lst.append(root.value)
            self.predecessor(root.right,lst)
        return lst

    def search(self,root,value):
        if root==None:
            print("value not found..")
        elif root.value==value:
            print("value found..")
        elif value<root.value:
            self.search(root.left,value)
        else:
            self.search(root.right,value)

    def delete(self,root,value):
        if root==None:
            return root
        elif value<root.value:
            root.left=self.delete(root.left,value)
        elif value>root.value:
            root.right=self.delete(root.right,value)
        elif value==root.value:
            if root.left==None and root.right==None:
                return None
            elif root.left and root.right:
                predecessor=self.predecessor(root.left).pop()
                root.value=predecessor
                root.left=self.delete(root.left,predecessor)
            else:
                if root.left and root.right==None:
                    root=root.left
                elif root.right and root.left==None:
                    root=root.right
            
        return root



obj=bst()
while True:
    n=int(input("1.insert 2.preorder 3.search 4.delete : "))
    if n==1:
        obj.root=obj.insert(obj.root,int(input("enter the value :")))
    elif n==2:
        lst=[]
        print(obj.preorder(obj.root,lst))
    elif n==3:
        obj.search(obj.root,int(input("enter the value : ")))
    elif n==4:
        obj.delete(obj.root,int(input("enter the value : ")))
    else:
        exit(0)
              
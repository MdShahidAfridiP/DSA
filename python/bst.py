class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class treenode:
    def __init__(self):
        self.root=None

    def create(self,value):
        self.root=node(value)
        print("value inserted at root.")

    def insert(self,head,value):
        if head.value:
            if value>head.value:
                if head.right:
                    return self.insert(head.right,value)
                else:
                    head.right=node(value)
                    print("node is inserted at right.")

            else:
                if head.left:
                    return self.insert(head.left,value)
                else:
                    head.left=node(value)
                    print("node is inserted at left.")
        else:
            self.create(value)

    def preorder(self,head):
        if head==None:
            return
        else:
            if head.value!=None:
                print(head.value)
            self.preorder(head.left)
            self.preorder(head.right)

    def inorder(self,head):
        if head==None:
            return
        else:
            self.inorder(head.left)
            print(head.value)
            self.inorder(head.right)

    def delete(self,head,val):
        if head.value==None:
            return
        elif val>head.value:
            self.delete(head.right,val)
        elif val<head.value:
            self.delete(head.left,val)
        elif val==head.value:
            temp=head
            while True:
                while temp.left:
                    temp=temp.left
                while temp.right:
                    temp=temp.right
                break
            head.value=temp.value
            temp.value=None

    def postorder(self,head):
        if head==None:
            return
        else:
            self.postorder(head.left)
            self.postorder(head.right)
            print(head.value)

    def levelorder(self,head):
        queue=[]
        if head==None:
            return
        else:
            queue.append(head)
            while len(queue)>0:
                print(queue[0].value)
                node=queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


obj=treenode()
while True:
    n=int(input("1.create 2.insert 3.preorder 4.inorder 5.postorder 6.delete 7.exit  : "))
    if n==1:
        obj.create(int(input("enter the value : ")))
    elif n==2:
        obj.insert(obj.root,int(input("enter the value : ")))
    elif n==3:
        obj.preorder(obj.root)
    elif n==4:
        obj.inorder(obj.root)
    elif n==5:
        obj.postorder(obj.root)
    elif n==6:
        obj.delete(obj.root,int(input("enter the value to delete : ")))
    elif n==7:
        obj.levelorder(obj.root)
    else:
        pass

# stack=[]
# while True:
#     print("1.push 2.pop 3.exit")
#     n=int(input("enter your choice :"))
#     if n==1:
#         stack.append(input("enter the braces :"))
#         print(stack)
#     elif n==2:
#         stack.pop()
#         print(stack)
#     else:
#         exit(0)


'''class node:
        def __init__(self,value):
                self.value=value
                self.next=None
'''
class stack:
        def __init__(self):
                self.head=None
        
        def push(self):
                new=node(int(input("enter the value : ")))
                if self.head==None:
                        self.head=new
                else:
                        new.next=self.head
                        self.head=new
        
        def pop(self):
                if self.head==None:
                        print("stack is empty")
                else:
                        print(self.head.value," popped")
                        self.head=self.head.next
        
        def traverse(self):
                temp=self.head
                while temp:
                        print(temp.value)
                        temp=temp.next
        
'''obj=stack()
while True:
        n=int(input("1.insert 2.pop 3.traverse : "))
        if n==1:
                obj.push()
        elif n==2:
                obj.pop()
        elif n==3:
                obj.traverse()
        else:
                exit(0) '''

class queue:
        def __init__(self):
                self.head=None
                self.tail=None
        
        def enqueue(self):
                new=node(int(input("enter the value : ")))
                if self.head==None:
                        self.head=new
                        self.tail=new
                else:
                        self.tail.next=new
                        self.tail=new
        
        def dequeue(self):
                if self.head==None:
                        print("queue is empty")
                else:
                        print(self.head.value," dequeued")
                        self.head=self.head.next

        def traverse(self):
                temp=self.head
                while temp:
                        print(temp.value)
                        temp=temp.next

'''obj=queue()
while True:
        n=int(input("1.enqueue 2.dequeue 3.traverse : "))
        if n==1:
                obj.enqueue()
        elif n==2:
                obj.dequeue()
        elif n==3:
                obj.traverse()
        else:
                exit(0)'''

class node:
        def __init__(self,value):
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
                                        lst.append(temp.right)

        def preorder(self,root):
                if root==None:
                        return
                else:
                        print(root.value)
                        self.preorder(root.left)
                        self.preorder(root.right)

        def delete(self,value):
                lst=[self.root]
                while len(lst):
                        temp=lst.pop(0)
                        if temp.left:
                                lst.append(temp.left)
                        if temp.right:
                                lst.append(temp.right)
                lst1=[self.root]
                while len(lst1):
                        temp1=lst1.pop(0)
                        if temp1.value==value:
                                temp1.value=temp.value                        
                        if temp1.left==temp:
                                temp1.left=None
                        elif temp1.left:
                                lst1.append(temp1.left)
                        if temp1.right==temp:
                                temp1.right=None
                        elif temp1.right:
                                lst.append(temp1.right)     

obj=tree()
while True:
        n=int(input("1.insert 2.delete 3.traverse : "))
        if n==1:
                obj.insert(int(input("enter the value :")))
        elif n==2:
                obj.delete(int(input("enter the value :")))
        elif n==3:
                obj.preorder(obj.root)
        else:
                exit(0)                   

class node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None

class sllist:
    head=None
    def insert(self,pos):
        new=node(int(input("enter the value : ")))
        temp=self.head
        if self.head!=None:
            if pos==0:
                new.next=self.head
                self.head=new
                print("node has inserted at head")
            else:
                for i in range(pos-1):
                    temp=temp.next
                new.next=temp.next
                new.prev=temp
                temp.next=new
                print("node has been inserted")
        else:
            self.head=new
            print("node has been inserted at head")

    def traversef(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()

    def traverseb(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data,end=" ")
            temp=temp.prev
        print()

    def delete(self,pos):
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        temp.next=temp.next.next
        if temp.next==None:
            pass
        else:
            temp.next.prev=temp

obj=sllist()
while True:
    n=int(input("1.insert 2.traverse 3.delete 4.exit: "))
    if n==1:
        obj.insert(int(input("enter the position : ")))
    elif n==2:
        obj.traversef()
        obj.traverseb()
    elif n==3:
        obj.delete(int(input("enter the position : ")))
    else:
        exit(0)
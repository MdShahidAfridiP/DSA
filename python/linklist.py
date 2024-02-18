class student:
    def __init__(self):
        self.name=""
        self.usn=""
        self.branch=""
        self.phone=None
        self.next=None
        self.prev=None
if __name__ == '__main__':

    head=None
    while(True):
        n = int(input("0.create \n 1.insert \n 2.display \n 3.reverse\n Enter your choice :"))
        if n==0:
            node=student()
            head=node
            node.name=input("name :")
            node.usn=input("usn :")
            node.branch=input("branch :")
            node.phone=input("phone :")
            node.next=None
            node.prev=None
        elif n==1:
            node1=student()
            node1.name = input("name :")
            node1.usn = input("usn :")
            node1.branch = input("branch :")
            node1.phone = input("phone :")
            node1.next=head
            node1.next.prev=node1
            head=node1
        elif n==2:
            temp=head
            while temp:
                print(f"name={temp.name},usn={temp.usn},branch={temp.branch},phone={temp.phone}")
                temp=temp.next
        elif n==3:
            temp=head
            while(temp.next):
                temp=temp.next
            while(temp):
                print(f"name={temp.name},usn={temp.usn},branch={temp.branch},phone={temp.phone}")
                temp=temp.prev
        else:
            break
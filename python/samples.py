def even_odd(num):
    if num%2==0:
        return f'number {num} is even.'
    else:
        return f'number {num} is odd.'

#lst=[1,2,3,4,5,6,8,34,66,21]
#ans=list(map(even_odd,lst))
#print(ans)

def fact(num):
    if num<=1:
        return 1
    else:
        num=num*fact(num-1)
    return num

#print(fact(5))

def prime(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
           count+=1
        else:
            pass
    if count==2:
        return f'number {num} is prime.'
    else:
        return 'number {} is not prime'.format(num)

#print(prime(4))

def largest(lst):
    large=0
    for i in lst:
        if i>large:
            large=i
        else:
            pass
    return large

#print(largest([1,6,2,4,6,7,5,33,21,65,44]))

def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b

#print('before swapping a={} b={}'.format(23,54))
#print('after swapping ',swap(23,54))

def fibo(n):
    a=0
    b=1
    count=0
    print(a,b,end=" ")
    for i in range(n):
        a=a+b
        b=a+b
        if a>n:
            exit(0)
        print(a,end=" ")
#fibo(56)

def palindrome_str(val):
    str=""
    for i in val:
        str=i+str
    if str==val:
        print(f"the given string {val} is pallindrome")
    else:
        print("string is not pallindrome")

#palindrome_str("radar")

def palindrome_num(val):
    temp,rev,org=0,0,val
    while val:
        temp=val%10
        rev=rev*10+temp
        val=val//10
    if rev==org:
        return "pallindrome"
    else:
        return "not pallindrome"

#print(palindrome_num(12321))

def leapyear(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return f"{year} is leap year"
    else:
        return "not a leap year"

#print(leapyear(2020))

def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if sum==num:
        return f'{num} is a perfect number'
    else:
        return 'not a perfect number'

#print(perfect(6))

def amstrong(num):
    temp,n,org=0,0,num
    while num:
        n=num%10
        temp=temp+n**3
        num=num//10
    if org==temp:
        return f'{org} is Amstrong.'
    else:
        return 'not an Amstrong number'

#print(amstrong(370))

def strong(num):
    temp,n,org=0,0,num
    while num:
        n=num%10
        temp=temp+fact(n)
        num=num//10
    if temp==org:
        return f'{org} is a strong number'
    else:
        return 'it is not a strong number'

#print(strong(145))

def reverse(num):
    rev,temp=0,0
    while num:
        rev=rev*10
        rev=rev+num%10
        num=num//10
    return rev

#print(reverse(34567))

def sum_of_digit(num):
    temp,res=0,0
    while num:
        temp=num%10
        res=res+temp
        num=num//10
    return res

#print(sum_of_digit(12345))

def lcm(a,b):
    if a<=b:
        mini=a
    else:
        mini=b
    while True:
        if mini%a==0 and mini%b==0:
            return mini
        else:
            mini+=1

#print(lcm(7,15))

def triangle(num):
    a=b=num*2//2
    for i in range(num):
        for j in range(num*2):
            if j<a or j>b:
                print("   ",end="")
            else:
                print(f" {i} ",end="")
        a-=1
        b+=1
        print()
#triangle(6)

def neon(num):
    rem=temp=org=0
    org=num
    temp1=num**2
    while temp1:
        rem=temp1%10
        temp=temp+rem
        temp1=temp1//10
    if temp==org:
        return 'neon'
    else:
        return 'not neon'
#print(neon(9))

def automorphic(num):
    temp=rem=0
    sq=num**2
    sq=str(sq)
    temp=len(str(num))
    if int(sq[-len(str(num)):]) == num:
        return 'automorphic'
    else:
        return 'not automorphic'
#print(automorphic(7))

def spy(num):
    sums=rem=0
    pro=1
    while num:
        rem=num%10
        sums=sums+rem
        pro=pro*rem
        num=num//10
    if sums==pro:
        return 'spy number'
    else:
        return 'not spy number'
#print(spy(2114))

'''class node:
    def __init__(self,value):
        self.prev=None
        self.value=value
        self.next=None'''

class ll:
    def __init__(self):
        self.head=None

    def create(self):
        new=node(int(input("enter the value : ")))
        self.head=new

    def insert(self,head,value):
        new=node(value)
        new.next=head
        head.prev=new
        self.head=new

    def forward_traverse(self,head):
        while head:
            print(head.value)
            head=head.next

    def backward_traverse(self,head):
        while head.next:
            head=head.next
        while head:
            print(head.value)
            head=head.prev

    def delete(self,head,value):
        while head.next:
            if head.next.value==value:
                head.next=head.next.next
                head.next.prev=head
            else:
                head=head.next
'''obj=ll()
while True:
    n=int(input("1.create 2.insert 3.forward_traverse 4.backward_traverse 5.delete : "))
    if n==1:
        obj.head=node(int(input("enter the value : ")))
    elif n==2:
        obj.insert(obj.head,int(input("enter the value : ")))
    elif n==3:
        obj.forward_traverse(obj.head)
    elif n==4:
        obj.backward_traverse(obj.head)
    elif n==5:
        obj.delete(obj.head,int(input("enter the value : ")))
    else:
        exit(0)'''



'''head=None
while True:
    n=int(input("1.create 2.insert 3.traverse 4.delete : "))
    if n==1:
        head=node(int(input("enter the value : ")))
    elif n==2:
        new=node(int(input("enter the value : ")))
        new.next=head
        head=new
    elif n==3:
        temp=head
        while temp:
            print(temp.value)
            temp=temp.next
    elif n==4:
        val=int(input("enter the value to delete : "))
        if head.value==val:
            head=head.next
        temp=head
        while temp.next:
            if temp.next.value==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
    else:
        exit(0) '''

class node:
    def __init__(self,value):
        self.left=None
        self.value=value
        self.right=None
        self.parent=None

class tree:
    def __init__(self):
        self.root=None
    def insert(self,head,value):
        if head==None:
            head=node(value)
        else:
            if head.value<=value:
                if head.right==None:
                    head.right=node(value)
                    head.right.parent=head
                else:
                    self.insert(head.right,value)
            else:
                if head.left==None:
                    head.left=node(value)
                    head.left.parent=head
                else:
                    self.insert(head.left,value)

    def preorder(self,head):
        if head==None:
            return
        else:
            print(head.value)
            self.preorder(head.left)
            self.preorder(head.right)

    '''def inorder(self,head):
        if head==None:
            return
        else:
            self.inorder(head.left)
            print(head.value)
            self.inorder(head.right)'''

    def postorder(self,head):
        if head==None:
            return
        else:
            self.postorder(head.left)
            self.postorder(head.right)
            print(head.value)

    def inorder(self,head):
        if head==None:
            return
        else:
            self.inorder(head.left)
            print(head.value)
            self.inorder(head.right)

    def bfs(self,head):
        queue=[]
        queue.append(head)
        while len(queue)>0:
            node=queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return queue.pop()

    def delete(self,head,val):
        if head.value == None:
            return
        elif val > head.value:
            self.delete(head.right, val)
        elif val < head.value:
            self.delete(head.left, val)
        elif val == head.value:
            if head.left:
                del_parent=self.inorder(head.left)
                head.value=del_parent.right.value
                #del_parent.parent.right=None
            else:
                del_parent=self.inorder(head.right)
                head.value=del_parent.left
                #del_parent.parent.left=None

obj=tree()
while True:
    n=int(input("1.create 2.insert 3.preorder 4.inorder 5.postorder : "))
    if n==1:
        obj.root=node(int(input("enter the value : ")))
    elif n==2:
        obj.insert(obj.root,int(input("enter the value : ")))
    elif n==3:
        obj.preorder(obj.root)
    elif n==4:
        obj.inorder(obj.root)
    elif n==5:
        obj.postorder(obj.root)
    elif n==6:
        obj.delete(obj.root,int(input("enter the value : ")))
    else:
        exit(0)
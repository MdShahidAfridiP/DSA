class array2:
    def __init__(self,rows,col):
        self.array=[0]*rows,[0]*col

    def insert(self,row,col):
        value=int(input("enter the value: "))
        if(self.array[row][col]==0):
            self.array[row][col]=value
            print("inserted successfully")
        else:
            print("already value existing : ",self.array[row][col])

    def delete(self,row,col):
        if (self.array[row][col] != 0):
            self.array[row][col]=0
        else:
            print("already value is 0")

    def traverse(self):
        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                print(self.array[i][j],end=" ")
            print()
obj=array2(int(input("enter the number of rows : ")),int(input("enter the number of columns : ")))
while(True):
    print("1.insert 2.delete 3.traverse 4.exit")
    choice=int(input("enter your choice : "))
    if choice==1:
        row=int(input("enter the row : "))
        col=int(input("enter the column :"))
        obj.insert(row,col)

    elif choice==2:
        row = int(input("enter the row : "))
        col = int(input("enter the column :"))
        obj.delete(row,col)

    elif choice==3:
        obj.traverse()

    elif choice==4:
        exit(0)

    else:
        exit(0)
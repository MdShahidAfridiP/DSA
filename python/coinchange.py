def coinchange(val):
    money=[1,2,5,10,20,50,100,200,500,2000]
    cost=[]
    i = len(money) - 1
    while True:
        if val>=money[i]:
            cost.append(money[i])
            val-=money[i]
        else:
            i-=1
        if val==0:
            return cost

def activityselection(tasks):
    print(tasks)
    tasks.sort()
    lst=[tasks.pop(0)]
    while tasks:
        key=tasks.pop(0)
        if key[0]>lst[len(lst)-1][1]:
            lst.append(key)
    print(lst)

tasks=[[5,6],[2,4],[1,2],[7,8],[3,4]]
activityselection(tasks)

values=coinchange(int(input("enter the amount : ")))
print("2000 rupees : ",values.count(2000))
print("500 rupees : ",values.count(500))
print("200 rupees : ",values.count(200))
print("100 rupees : ",values.count(100))
print("50 rupees : ",values.count(50))
print("20 rupees : ",values.count(20))
print("10 rupees : ",values.count(10))
print("5 rupees : ",values.count(5))
print("2 rupees : ",values.count(2))
print("1 rupees : ",values.count(1))
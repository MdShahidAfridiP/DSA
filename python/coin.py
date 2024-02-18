cases=int(input())
for i in range(1,cases+1):
    value=int(input())
    cc=0
    while value>=1:
        value=value//2
        cc=cc+1
    print(cc)
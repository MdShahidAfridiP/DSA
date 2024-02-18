import math
val=0
dic={}
for i in range(int(input())):
    x,y,s=map(int,input().split())
    t=math.sqrt(((x/s)**2+(y/s)**2))
    if(dic.get(t)==None):
        dic[t]=1
    else:
        dic[t]+=1
for i in dic:
    if(dic[i]!=1):
        val+=(dic[i]*(dic[i]-1))/2
print(int(val))
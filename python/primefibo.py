def prime(n1,n2):
    lst=[]
    for num in range(n1,n2+1):
        if num>1:
            for i in range(2,num):
                if (num%i)==0:
                    break
            else:
                lst.append(num)
    return lst

def prime1(num):
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True

def fib(n,mini,maxi):
    lst=[] 
    a=mini
    b=maxi
    if (n >= 0): 
        lst.append(a) 
    if (n >= 1): 
        lst.append(b)
    for i in range(2, n+1): 
        c = a + b 
        lst.append(c) 
        a = b 
        b = c
    return lst[-1]

ip=list(map(int,input().split()))           
lst=prime(ip[0],ip[1])
newlst=[]
for j in range(len(lst)):
    for i in range(len(lst)-1):
        if lst[j]==lst[i]:
            continue
        if i<=len(lst):
            new=str(lst[j])+(str(lst[i+1]))
            newlst.append(new)
print(len(newlst))
newlst=list(map(int,newlst))
list2=list(filter(prime1,newlst))
mini=min(list2)
maxi=max(list2)
#print(mini,maxi,len(list2))
print(fib(len(list2),mini,maxi))
print(set(newlst).difference([23, 25, 27, 211, 213, 217, 219, 223, 229, 231, 32, 35, 37, 311, 313, 319, 323, 329, 331, 337, 52, 53, 57, 511, 513, 517, 519, 523, 529, 531, 537, 72, 73, 75, 711, 713, 717, 719, 723, 729, 731, 737, 112, 113, 115, 117, 1113, 1117, 1119, 1123, 1129, 1131, 1137, 132, 133, 135, 137, 1311, 1317, 1319, 1323, 1329, 1331, 1337, 172, 173, 175, 177, 1711, 1713, 1719, 1723, 1729, 1731, 1737, 192, 193, 195, 197, 1911, 1913, 1917, 1923, 1929, 1931, 1937, 232, 233, 235, 237, 2311, 2313, 2317, 2319, 2329, 2331, 2337, 292, 293, 295, 297, 2911, 2913, 2917, 2919, 2923, 2931, 2937, 312, 315, 317, 3111, 3113, 3117, 3119, 3123, 3129, 3137, 372, 373, 375, 377, 3711, 3713, 3717, 3719, 3723, 3729, 3731]))
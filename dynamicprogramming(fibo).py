calc = 0
def fiboslow(n):
    global calc
    calc += 1
    if n<=2:
        return n
    else:
        return fiboslow(n-1) + fiboslow(n-2)
print("Fibonacci slow : ",fiboslow(20))
print("total calc : ",calc)

dynrecords = {}
calc = 0
def fibofast(n):
    global dynrecords, calc
    calc += 1
    if dynrecords.get(n):
        return dynrecords[n]
    elif n<=2:
        return n
    else:
        dynrecords[n] = fibofast(n-1) + fibofast(n-2)
        return dynrecords[n]
    
print("Fibonacci fast : ",fibofast(20))
print("total calc : ",calc)
print("dynamic records : ", dynrecords)
import matplotlib.pyplot as plt
import numpy as np
shahid=[500,230,599,346,500]
fardeen=[543,379,236,559,450]
x=list(range(1,6))
plt.plot(x,shahid,label="Shahid Marks",color='c',marker='o',markerfacecolor='r',linestyle="solid")
plt.plot(x,fardeen,label="fardeen Marks",color='r',marker='o',markerfacecolor='c',linestyle="solid")
plt.xlabel("semesters")
plt.ylabel("marks")
plt.xticks([1,2,3,4],["1st sem","2st sem","3st sem","4st sem"])
plt.legend(loc="upper left")
plt.title("my marks of all semester")
plt.grid(True)
plt.show()



first=[14,9,15,7,5,12]
sub=[1,2,3,4,5,6]
second=[15,10,15,14,11,11]
mid=[]
for i in range(len(first)):
    mid.append(np.mean(list([first[i],second[i]])))


plt.plot(sub,first,label="IA 1",color="c",marker="o",markerfacecolor="r")
plt.plot(sub,second,label="IA 2",color="r",marker="o",markerfacecolor="c")
plt.plot(sub,mid,label="mid",color="g",marker="o",markerfacecolor="b")
plt.xlabel("subjects")
plt.ylabel("marks")
plt.xticks([1,2,3,4,5,6],["English","kannada","hindi","maths","science","social"])
plt.legend(loc="upper left")
plt.title("Saniya Marks")
plt.grid(True)
plt.show()
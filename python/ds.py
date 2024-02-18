class node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None
    
class ll:
    def __init__(self):
        self.head=None
    
    def insert(self,head,value):
        if head==None:
            head=node(value)
        else:
            head.next=self.insert(head.next,value)
            head.next.prev=head
        return head
    
    def traverse(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def reverse(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data)
            temp=temp.prev

    def delete(self,head,value):
        if head.data==value:
            return head.next
        else:
            head.next=self.delete(head.next,value)
            head.next.prev=head
        return head

'''obj=ll()
while True:
    n=int(input("1.insert 2.traverse 3.delete 4.reverse : "))
    if n==1:
        obj.head=obj.insert(obj.head,int(input("enter the value :")))
    elif n==2:
        obj.traverse()
    elif n==3:
        obj.head=obj.delete(obj.head,int(input("enter the value to delete :")))
    elif n==4:
        obj.reverse() '''

def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 # Finding the mid of the array 
		L = arr[:mid] # Dividing the array elements 
		R = arr[mid:] # into 2 halves 

		mergeSort(L) # Sorting the first half 
		mergeSort(R) # Sorting the second half 

		i = j = k = 0
		
		# Copy data to temp arrays L[] and R[] 
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+= 1
			else: 
				arr[k] = R[j] 
				j+= 1
			k+= 1
		
		# Checking if any element was left 
		while i < len(L): 
			arr[k] = L[i] 
			i+= 1
			k+= 1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+= 1
			k+= 1
# nlist=[14,46,43,27,57,41,45,21,70]
# mergeSort(nlist)
# print(nlist)

def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]

    return i+1

def quicksort(arr,low,high):
    if low<high:
        pivot=partition(arr,low,high)
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)

# nlist = [14,46,43,27,57,41,45,21,70]
# quicksort(nlist,0,len(nlist)-1)
# print(nlist)

import sys
class graph:
    def __init__(self,n):
        self.V=n
        self.graph=[[]]

    def minvertex(self,dist,sptset):
        min=sys.maxsize
        for v in range(self.V):
            if dist[v]<min and sptset[v]==False:
                min=dist[v]
                index=v
        return index

    def dijkstra(self,scr):
        dist=[sys.maxsize]*self.V
        dist[scr]=0
        sptset=[False]*self.V

        for cout in range(self.V):
            last=self.minvertex(dist,sptset)
            sptset[last]=True
            for v in range(self.V):
                if self.graph[last][v]>0 and sptset[v]==False and dist[v]>dist[last]+self.graph[last][v]:
                    dist[v]=dist[last]+self.graph[last][v]

        print(dist)

g = graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
		[4, 0, 8, 0, 0, 0, 0, 11, 0], 
		[0, 8, 0, 7, 0, 4, 0, 0, 2], 
		[0, 0, 7, 0, 9, 14, 0, 0, 0], 
		[0, 0, 0, 9, 0, 10, 0, 0, 0], 
		[0, 0, 4, 14, 10, 0, 2, 0, 0], 
		[0, 0, 0, 0, 0, 2, 0, 1, 6], 
		[8, 11, 0, 0, 0, 0, 1, 0, 7], 
		[0, 0, 2, 0, 0, 0, 6, 7, 0] 
		]; 

g.dijkstra(0);
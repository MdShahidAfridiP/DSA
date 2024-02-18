def mergeSort(nlist):       #[14,46,43,27,57,41,45,21,70]
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",nlist)

#mergeSort([14,46,43,27,57,41,45,21,70])

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    # Driver code to test above

# nlist = [14,46,43,27,57,41,45,21,70]
# quickSort(nlist,0,len(nlist)-1)
# print(nlist)

import sys

class graph():
    def __init__(self,v):
        self.V=v
        self.graph=[[]]

    def mindistance(self,dist,sptset):
        min=sys.maxsize
        for v in range(self.V):
            if dist[v]<min and sptset[v]==False:
                min=dist[v]
                index=v
        return index

    def dijkstra(self,src):
        dist=[sys.maxsize]*self.V
        dist[src]=0
        sptset=[False]*self.V

        for cout in range(self.V):
            u=self.mindistance(dist,sptset)
            sptset[u]=True
            for v in range(self.V):
                if self.graph[u][v]>0 and sptset[v]==False and dist[v]>dist[u]+self.graph[u][v]:
                    dist[v]=dist[u]+self.graph[u][v]

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
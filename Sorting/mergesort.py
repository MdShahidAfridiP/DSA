def MergeSort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        left_half = MergeSort(left_arr)
        right_half = MergeSort(right_arr)
        return Merge(left_half, right_half)

def Merge(left, right):
    merge = []
    left_index, right_index = 0,0
    while(left_index<len(left) and right_index<len(right)):
        if left[left_index]<right[right_index]:
            merge.append(left[left_index])
            left_index+=1
        else:
            merge.append(right[right_index])
            right_index+=1
    merge.extend(left[left_index:])
    merge.extend(right[right_index:])
    return merge


# Example usage:
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = MergeSort(arr)
print("Sorted array:", sorted_arr)
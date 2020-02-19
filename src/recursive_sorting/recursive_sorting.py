# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    lenA = len(arrA)
    lenB = len(arrB)
    i = 0
    j = 0
    k = 0

    while (i < lenA and j < lenB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
            k += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
            k += 1
    while (i < lenA):
        merged_arr[k] = arrA[i]
        i += 1 
        k += 1
    while (j < lenB):
        merged_arr[k] = arrB[j]
        j += 1 
        k += 1

    return merged_arr

#merge([1, 2, 3, 34, 102], [1, 6, 7, 23, 34])

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr 
    midpoint = (len(arr)) // 2
  
    left = merge_sort(arr[:midpoint])
    right = merge_sort(arr[midpoint:])
   
    #     
    arr = merge(left, right)
    return arr

merge_sort([5, 2, 23, 42, 1, 8, 12, 9])

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

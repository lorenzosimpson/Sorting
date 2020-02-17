# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
       
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j        
        arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(0, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[i]:
                    arr[j], arr[i] = arr[i], arr[j]
                else:
                    swapped = False
    return arr



# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
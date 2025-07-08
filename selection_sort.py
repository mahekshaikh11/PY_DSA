def selection_sort (arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
               min_index = j

         #SWAP WITH MIN NO.
        arr[i],arr[min_index] = arr[min_index],arr[i]

    return arr  

arr = [22,67,34,9,90]     
selection_sort(arr)
print (arr)     
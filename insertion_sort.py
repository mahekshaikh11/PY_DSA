def insertion_sort(arr):
    for i in range (1,len(arr)):
        key = arr[i]
        j =i-1
        while j>=0 and key <arr[j]:
            arr[j+1]=arr[j]
            j -=1
        arr[j+1]=key
        return arr

arr = [47,34,9,0,50,0,38,36,11,10] 

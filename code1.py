#how much max swap needed to sort array of lenght 6?

def bubble_sort(arr):
    n=len(arr)
    count =0

    for i in range(n-1):
        is_sorted = True
        for j in range (n-i-1):
            if (arr[j]>arr[j+1]):
                is_sorted = False
                count = count+1
                #left more than right then swap
                arr[j],arr[j+1]=arr[j+1],arr[j]
            if is_sorted:
                break
    return count

print(bubble_sort([7,3,5,2,1]))            
def merge_2sorted_array(arr1, arr2):
    i, j = 0,0
    merged = []

    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i = i+1
        else:
            merged.append(arr2[j])
            j = j+1
    
    while i<len(arr1):
        merged.append(arr1[i])
        i+=1
    while j<len(arr2):
        merged.append(arr2[j])
        j+=1
    return merged 

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    #merge 2 sorted arrays
    return merge_2sorted_array(left, right)

def binary_search_helper(arr, start, end, key):
    if start > end:
        return -1
     
    mid = (start+end)//2
    if arr[mid] == key:
         return mid
    elif key > arr[mid]:
        return binary_search_helper(arr, mid+1, end, key)
    else:
        return binary_search_helper(arr, start, mid-1, key)


def binary_search(arr, key):
    return binary_search_helper(arr,0,len(arr)-1, key)


if __name__ == '__main__':
    arr = [9,3,4,2,0]
    #sorting
    # arr = merge_sort(arr)
    index = binary_search(arr, 9)
    print(f"{index}")

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array is:", arr)

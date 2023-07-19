def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    greater_than_pivot = [x for x in arr[1:] if x > pivot]

    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


# Example usage:
input_str = input("Enter the items to be sorted (separated by commas): ")
arr = [int(item) for item in input_str.split(",")]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)


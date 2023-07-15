def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_idx = i

        # Find the index of the smallest element in the unsorted subarray
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the smallest element with the first element of the unsorted subarray
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Example usage:
arr = [5, 2, 9, 1, 7, 6]
selection_sort(arr)
print("Sorted array:", arr)

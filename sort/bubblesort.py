def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        # Last i elements are already sorted
        for j in range(n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
arr = [5, 2, 9, 1, 7, 6]
bubble_sort(arr)
print("Sorted array:", arr)


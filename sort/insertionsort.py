def insertion_sort(arr):
    # Convert input string to a list of integers
    arr = [int(num) for num in arr.split(",")]

    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Shift elements greater than the key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Example usage:
input_str = input("Enter the numbers to be sorted (separated by commas): ")
sorted_arr = insertion_sort(input_str)
print("Sorted array:", sorted_arr)


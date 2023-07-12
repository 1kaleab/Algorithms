def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target element not found

# Example usage:
arr = [1, 2, 5, 6, 7, 9]
target = 7

result = binary_search(arr, target)
if result != -1:
    print(f"Target element found at index {result}")
else:
    print("Target element not found in the array")


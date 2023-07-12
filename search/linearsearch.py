def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Target element not found

# Example usage:
arr = [5, 2, 9, 1, 7, 6]
target = 7

result = linear_search(arr, target)
if result != -1:
    print(f"Target element found at index {result}")
else:
    print("Target element not found in the array")


def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# Read input
data = list(map(int, input().split()))
n = data[0]
arr = data[1:]

reverse_array(arr)

# Print reversed array
print(*arr)

def grow(arr):
    result = 1
    for i in range(len(arr)):
        result = result * arr[i]
    return result

print(grow([4, 1, 1, 1, 4]))
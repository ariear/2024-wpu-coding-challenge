def first_non_consecutive(arr):
    for a in range(len(arr)):
        current = arr[a]
        if a < len(arr) - 1:
            second = arr[a + 1]
            if current + 1 != second:
                return second
        else:
            return None

print(first_non_consecutive([1,2,3,4,6,7,8]))
print(first_non_consecutive([4,5,6,7,8,9,11]))
print(first_non_consecutive([-3,-2,0,1]))
print(first_non_consecutive([-5,-4,-3,-1]))
print(first_non_consecutive([1,2,3,4,5,6,7,8]))
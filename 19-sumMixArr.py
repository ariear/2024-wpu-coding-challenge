def sum_mix(arr):
    result = 0
    for i in range(len(arr)):
        result = result + int(arr[i])
    return result

print(sum_mix([9, 3, '7', '3']))
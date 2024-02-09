def sum_array(arr):
    if type(arr) != list or len(arr) <= 2:
        return 0
    
    sorting = sorted(arr)
    sorting.remove(sorting[0])
    sorting.pop()
    return sum(sorting)
    
print(sum_array([6, 2, 1, 8, 10]))
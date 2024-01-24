def count_sheep(n):
    result = ''
    for i in range(1, n + 1): result = result + str(i) + ' sheep...'
    return result

print(count_sheep(3))
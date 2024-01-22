def reverse_seq(n):
    result = [n]
    for i in range(n, 1, -1):
        result.append(i - 1)
    return result

print(reverse_seq(5))
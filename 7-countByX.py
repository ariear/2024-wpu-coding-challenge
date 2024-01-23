def count_by(x, n):
    result = [x]
    for i in range(n - 1):
        result.append(result[i] + x)
    return result

print(count_by(1, 5))
print(count_by(2, 5))
print(count_by(3, 5))
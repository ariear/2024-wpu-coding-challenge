def remove_every_other(my_list):
    results = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            results.append(my_list[i])
    return results

print(remove_every_other(['Hello', 'Remove', 'Hello', 'Remove']))
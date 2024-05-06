def str_count(strng, letter):
    count = 0
    for i in range(len(strng)):
        if strng[i] == letter:
            count += 1
    return count

print(str_count("Hello", "l"))
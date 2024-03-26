def update_light(current):
    lists = {
        'green': 'yellow',
        'yellow': 'red',
        'red': 'green'
    }
    return lists[current]

print(update_light('green'))
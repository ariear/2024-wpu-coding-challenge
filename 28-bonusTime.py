def bonus_time(salary, bonus):
    return f'${salary * 10}' if bonus else f'${salary}'

print(bonus_time(2500, True))
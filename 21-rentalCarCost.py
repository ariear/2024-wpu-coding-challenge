def rental_car_cost(d):
    if d >= 3 and d <= 4:
        return d * 40 - 20
    elif d >= 5:
        return d * 40 - 50
    return d * 40

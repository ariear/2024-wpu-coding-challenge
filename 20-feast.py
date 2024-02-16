def feast(beast, dish):
    return True if beast[0] == dish[0] and beast[len(beast) - 1] == dish[len(dish) - 1] else False

print(feast("great blue heron", "garlic naan"))
print(feast("brown bear", "bear claw"))
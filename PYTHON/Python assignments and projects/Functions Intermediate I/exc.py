# import random
# def randInt(min= 50, max=500 ):
#     num = random.random()*100
#     return num
# print(randInt())             # should print a random integer between 0 to 100
# print(randInt(max=50))         # should print a random integer between 0 to 50
# print(randInt(min=50))         # should print a random integer between 50 to 100
# print(randInt(min=50, max=500))    # should print a random integer between 50 and 500


import random

def randInt(min=0, max=100):
    # BONUS: Handle edge cases
    if min > max:
        min, max = max, min  # Swap if min is greater than max
    if max < 0:
        max = 0

    # Calculate random float in range and round to integer
    num = round(random.random() * (max - min) + min)
    return num

# Test Cases
print(randInt())                    # Random integer between 0 and 100
print(randInt(max=50))              # Random integer between 0 and 50
print(randInt(min=50))              # Random integer between 50 and 100
print(randInt(min=50, max=500))     # Random integer between 50 and 500
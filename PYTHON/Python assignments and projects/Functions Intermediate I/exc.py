import random
def randInt(min=0,max=1):
    num = random.random()
    return num
print(randInt())             # should print a random integer between 0 to 1


import random
def randInt(min=0,max=50):
    num = round(random.random()*(max - min) + min)
    return num
print(randInt())             # should print a random integer between 0 to 50


import random
def randInt(min=10,max=35):
    num = round(random.random()*(max - min) + min)
    return num
print(randInt())             # should print a random integer between 10 to 35









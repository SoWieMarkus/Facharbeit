import random
import math

def getRandomNumber():
    return random.randint(0, radius)

radius = 100
totalAmountOfHits = 100000

for i in range (0, 100000):
    hitsInsideCircleArea = 0

    for i in range(0,totalAmountOfHits):
        x = getRandomNumber()
        y = getRandomNumber()
        r = math.sqrt(x*x + y*y)
        print("r " + str(r))
        if r <= radius:
            hitsInsideCircleArea += 1

    print("Pi: " + str(4*hitsInsideCircleArea/totalAmountOfHits))


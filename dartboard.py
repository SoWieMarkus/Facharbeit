import random
import math

radius = 100

def getRandomNumber():
    return random.randint(0, radius)

def calculatePi(totalAmountOfHits):
    
    hitsInsideCircleArea = 0

    for i in range(0,totalAmountOfHits):
        x = getRandomNumber()
        y = getRandomNumber()
        r = math.sqrt(x*x + y*y)
        if r <= radius:
            hitsInsideCircleArea += 1

    return 4* hitsInsideCircleArea / totalAmountOfHits

def main():
    for i in range (1, 100):
        pi =  calculatePi(i)
        print("Pi based on "+ str(i) + " hits: " + str(pi))


if __name__ == "__main__":
    main()


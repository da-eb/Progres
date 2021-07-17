import random
import time

def koin():
    heads = "HEADS"
    tails = "TAILS"
    flips = 0
    tossed = int(input("Number of times to toss the coin :   "))
    flip = []

    heads_and_tails = [(heads),(tails)]

    while input("To Toss the coin press Y or N: ").lower() == "y":
        if flips != tossed:
            rand = (random.choice(heads_and_tails))
            print(rand)

            time.sleep(.5)
            flips +=1
            flip.append(rand)
        elif flips ==tossed: break
    print(f"You flipped the coin {flips} times")
    print("Good bye")
    print(flip)
 
        
koin()

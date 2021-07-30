import random
from datetime import datetime

if __name__ == '__main__':
    alive_counter = 0
    highest_alive_counter = 0
    num_tries = 0

    while True:

        # Increase number of tries
        num_tries = num_tries + 1

        # Generate random number and compare to 0.5 to simulate 50/50 odds
        if random.random() <= 0.5:

            # If random number is less than or equal 0.5, the object is alive.
            alive_counter = alive_counter + 1

            if alive_counter > highest_alive_counter:
                # Update highest counter
                highest_alive_counter = alive_counter
                print("Number of tries: " + "{:,}".format(num_tries))
                print("Highest counter: " + str(highest_alive_counter))

                # Calculate chances of the highest counter happening
                percent_chances_happening = pow(0.5, highest_alive_counter) * 100
                print("Chances of this happening is: " + '{0:.300f}'.format(percent_chances_happening).rstrip('0').rstrip('.') + "% - " + str(datetime.now()))
                print("-------------------")
        else:
            # else reset counter if object is dead.
            alive_counter = 0

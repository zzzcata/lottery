import random

print "Welcome to the Lottery numbers generator."

def lottery():
    while True:
        choose_number = int(raw_input("Please enter how many random numbers would you like to have (from 1 to 49): "))
        n = choose_number
        if n > 49 or n < 1:
            print "Number is not in range. Try again!"
        else:
            return random.sample(range(1, 49), n)
            break

print lottery()
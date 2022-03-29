import random


def swap1(option, option2):
    if option > option2:
        option2, option = option, option2  # swap values
    print(option, option2)  # return 2 values


def swapTester():
    # implement 10 tests of the swap function
    for i in range(10):
        # generate random numbers as test cases
        x = random.randint(0, 200)
        y = random.randint(0, 500)
        swap1(x, y)

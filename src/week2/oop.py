import random


class FindGCD:
    # All Python classes have a function called init(), which is always executed when the class is called and the
    # resulting object is constructed.
    def __init__(self):
        pass

    # Function to find the GCD of two Numbers
    def __call__(self, num1, num2):
        if num1 == 0:
            return num1
        while num2 != 0:
            if num1 > num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
        return num1


# OOP Tester
def gcdTester():
    # run 20 tests
    for i in range(20):
        x = random.randrange(0, 200)
        y = random.randrange(0, 500)
        myInstance = FindGCD()
        z = myInstance(x, y)
        # print result of every test
        print("The greatest common denominator of %d and %d is %d" % (x, y, z))


# Imperative Form
# Function to find the GCD of two Numbers
def findgcd(num1, num2):
    if num1 == 0:
        return num1
    while num2 != 0:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


def gcd():
    a = int(input(" Enter the First Value for GCD: "))
    b = int(input(" Enter the Second Value for GCD: "))
    gcd = findgcd(a, b)
    print("\n GCD of {0} and {1} is: {2}".format(a, b, gcd))
    print()


if __name__ == "__main__":
    gcd()
    gcdTester()

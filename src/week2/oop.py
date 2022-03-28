class FindGCD:
    # All Python classes have a function called init(), which is always executed when the class is called and the
    # resulting object is constructed.
    def __init__(self):
        self.num1 = num1
        self.num2 = num2


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

# Hack 2: Write Factorial function using classes, providing implementation of call.
class Factorial:
    # All Python classes have a function called init(), which is always executed when the class is called and the
    # resulting object is constructed

    # The call function/method is a special to Python, when implemented inside a class, this gives its object the
    # ability to behave like a regular Python function.
    def __call__(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f


# prints out the final number of the factorial sequence
print("Enter a Number: ", end="")
num = int(input())

ob = Factorial()
print("\nFactorial of", num, "=", ob(num))


# Factorial tester
def facTester():
    for i in range(11):
        # create instance of class
        myOb = Factorial()
        # calculate factorial of i
        answer = myOb(i)
        print("The factorial of %d is %d" % (i, answer))


if __name__ == "__main__":
    Factorial()
    facTester()

# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with
# try/except) for invalid input
def fibonacci():
    count = int(input("Enter fibonacci sequence count: "))
    n = 0
    while True:
        if n <= count:
            try:
                print(fibonacci1(n), end=" ")
                n += 1
                print()

            except ValueError:
                print('Invalid input. Please enter an integer input.')
        else:
            return


def fibonacci1(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return fibonacci1(n - 1) + fibonacci1(n - 2)


if __name__ == "__main__":
    fibonacci()

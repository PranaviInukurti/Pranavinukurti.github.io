def tree():
    n = int(input("Enter the height of your tree: "))
    # number of spaces
    k = n - 1
    # outer loop to handle number of rows
    for i in range(0, n):
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
        # decrementing k after each loop
        k = k - 1
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")
        # ending line after each row
        print(" ")
    # width of stump
    trunk = n // 4
    # rows of stump
    trunk_height = n // 6
    for i in range(trunk_height):
        # trunk must be centered
        for j in range(n - trunk):
            print(" ", end="")
        for k in range(trunk):
            print("*", end="")
        print("  ")


if __name__ == "__main__":
    tree()

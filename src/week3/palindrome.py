class Palindrome:
    def __init__(self):
        pass

    def __call__(self, n):
        # no capital letters
        x = n.lower()
        # remove spaces
        x = x.replace(" ", "")
        # remove special characters
        x = filter(str.isalpha, x)
        x = "".join(x)
        # tests = characters / 2, if it's odd then it only needs characters - 1 / 2 => len(x)//2
        for i in range(len(x) // 2):
            # compare characters
            if x[i] == x[len(x) - 1 - i]:
                continue
            else:
                return n + " is not a palindrome because " + x[i] + " and " + x[len(x) - 1 - i] + " don't match"
        # if all tests passed
        return n + " is a palindrome"


def palTester():
    # test cases
    tests = ["A man, a plan, a canal -- Panama!", "kayak", "cool", "my gym", "Never Odd or Even",
             "I did, did I?", "Don't nod.", "Sit on a potato pan, Otis.", "kick", "penelope",
             "tac0cat", "RaCeCaR", "nurses run", "Step on no pets", "pulp"]
    for i in tests:
        # test every string
        obj = Palindrome()
        print(obj(i))

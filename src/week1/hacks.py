import time

# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as
# illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "Pranavi",
    "LastName": "Inukurti",
    "DOB": "November 19",
    "POB": "California",
    "Email": "pranukurti@gmail.com",
    "Favorite_foods": ["Chole Bhatura", "Pav bhaji", "Fajita"]
})

InfoDb.append({
    "FirstName": "Ridhima",
    "LastName": "Inukurti",
    "DOB": "January 10",
    "POB": "Hyderabad",
    "Email": "rinukurti@gmail.com",
    "Favorite_foods": ["Pani Puri", "Burrito", "Pizza"]
})

InfoDb.append({
    "FirstName": "Siva Kumar",
    "LastName": "Inukurti",
    "DOB": "December 18",
    "POB": "Nellore",
    "Email": "siva.inukurthi@gmail.com",
    "Favorite_foods": ["Bisi Bele Bath", "Puri"]
})

InfoDb.append({
    "FirstName": "Sirisha",
    "LastName": "Guntupalli",
    "DOB": "May 04",
    "POB": "Vijayawada",
    "Email": "guntupallisri@gmail.com",
    "Favorite_foods": ["Dosa", "Samosa"]
})


# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Favorite foods: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Favorite_foods"]))  # join allows printing a string list with separator
    print()


# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)


# for loop iterates on length of InfoDb
# change the while loop to move argument n inside the definition
def while_loop():
    n = 0
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return


def recursive_loop():  # removed all the arguments
    # Made new function to call recursively
    n = 0
    recursive_loop1(n)
    return


def recursive_loop1(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop1(n + 1)
    return  # exit condition


def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop()  
    print("Recursive loop")
    recursive_loop()


if __name__ == "__main__":
    tester()

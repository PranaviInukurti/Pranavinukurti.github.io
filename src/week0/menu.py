"""
Introduction to Console Programming
Writing a function to print a menu
"""


# Menu options in print statement
def print_menu1():
    print('1 -- Dosa')
    print('2 -- Samosa Chat')
    print('3 -- Mango Lassi')
    print('4 -- Bisi Bele Bath')
    print('5 -- Exit')
    runOptions()


# Menu options as a dictionary
menu_options = {
    1: 'Dosa',
    2: 'Samosa Chat',
    3: 'Mango Lassi',
    4: 'Bisi Bele Bath',
    5: 'Exit',
}


# Print menu options from dictionary key/value pair
def print_menu2():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])
    runOptions()


# menu option 1
def one():
    print('Enjoy your \'Dosa\'')


# menu option 2
def two():
    print('Enjoy your \'Samosa Chat\'')


# menu option 3
def three():
    print('Enjoy your \'Mango Lassi\'')


def four():
    print('Enjoy your \'Bisi Bele Bath\'')


def swap1(option, option2):
    if option > option2:
        option2, option = option, option2  # swap values
    return option, option2  # return 2 values


def swap1_helper(option, option2):
    print("This is your order: ", option, option2)
    option, option2 = swap1(option, option2)
    print("We recommend you consume them in this order: ", option, option2)
    print()
    # no return value


# call functions based on input choice
def runOptions():
    # infinite loop to accept/process user menu choice
    while True:
        try:
            option = int(input('What would you like to eat for a meal today? (enter 1-4) '))
            if option == 1:
                one()
            elif option == 2:
                two()
            elif option == 3:
                three()
            elif option == 4:
                four()

            # Exit menu
            elif option == 5:
                print('Enjoy Your Meal! Good Bye...')
                exit()  # exit out of the (infinite) while loop
            option2 = int(input('What else would you like to order? (1-4)'))
            if option2 == 1:
                one()
            elif option2 == 2:
                two()
            elif option2 == 3:
                three()
            elif option2 == 4:
                four()

            else:
                print('Invalid option. Please enter a number between 1 and 4.')
            swap1_helper(option, option2)
        except ValueError:
            print('Invalid input. Please enter an integer input.')


if __name__ == '__main__':
    # print_menu1()
    print_menu2()
    swap1_helper()

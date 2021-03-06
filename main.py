import src.week0.swap
import src.week0.matrix
import src.week0.function_menu
import src.week0.ship
import src.week0.tree
import src.week1.hacks
import src.week1.fib
import src.week2.fac
import src.week2.oop
import src.week3.palindrome

main_menu = [
    ["Fibonacci", src.week1.fib.fibonacci],
    ["Matrix", src.week0.matrix.matrix],
    ["Menu", src.week0.function_menu.print_menu2],
    ["Palindrome", src.week3.palindrome.palTester],
    ["Ship", src.week0.ship.ship],
    ["Tree", src.week0.tree.tree]
]

math_sub_menu = [
    ["Factorial", src.week2.fac.facTester],
    ["Greatest Common Denominator", src.week2.oop.gcdTester],
    ["Swap", src.week0.swap.swapTester]
]

patterns_sub_menu = [
    ["For Loop", src.week1.hacks.for_loop],
    ["While Loop", src.week1.hacks.while_loop],
    ["Recursive Loop", src.week1.hacks.recursive_loop],
]

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Loops", patterns_submenu])
    menu_list.append(["Math", math_submenu])
    buildMenu(title, menu_list)


def submenu():
    title = "Function Submenu" + banner
    buildMenu("Math", sub_menu)


def patterns_submenu():
    title = "Patterns Submenu" + banner
    buildMenu(title, patterns_sub_menu)


def math_submenu():
    title = "Math Submenu" + banner
    buildMenu(title, math_sub_menu)


def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()

from week0 import christmastree
from week0 import ship
from week0 import keypad
from week0 import swap
from week1 import fibonacci
from week1.infodb import for_loop,while_loop,recursive_loop
from week2 import factorial
from week2 import prime
from week2 import palindrome
from crossover import game

def op1():
    print('Option 1')
def op2():
    print('Option 2')

def buildMenu(menu):
    for key,value in menu.items():
        display = value["display"]
        print(f"{key} ------ {display}")
    print("What is your choice? (enter the number value) ")

def presentMenu(menu):
    buildMenu(menu)
    choice = int(input())
    if (choice) in menu:
        if menu[choice]["type"] == "func":
            menu[choice]["exec"]()
        else:
            presentMenu(menu[choice]["exec"])

subMenu = {
    1: {"display":"Option 1",
        "exec":op1,
        "type":"func"},
    2: {"display":"Option 2",
        "exec":op2,
        "type":"func"}
}

InfoDB = {
    1: {"display":"For Loop",
        "exec": for_loop,
        "type":"func"},
    2: {"display":"While Loop",
        "exec": while_loop,
        "type":"func"},
    3: {"display":"Recursive Loop",
        "exec": recursive_loop,
        "type":"func"}
}

week0 = {
    1: {"display":"Christmas Tree",
        "exec":christmastree,
        "type":"func"},
    2: {"display":"Ship",
        "exec":ship,
        "type":"func"},
    3: {"display":"Keypad ",
        "exec":keypad.matrix_print,
        "type":"func"},
    4: {"display":"Swap ",
        "exec":swap,
        "type":"func"},
    5: {"display":"Submenu",
        "exec": subMenu,
        "type": "submenu"}
}

week1 = {
    1: {"display": "Fibonacci Sequence",
        "exec": fibonacci.printFibonacci,
        "type": "func"},
    2: {"display": "InfoDB",
        "exec": InfoDB,
        "type": "func"}
}

week2 = {
    1: {"display": "Factorial",
        "exec": factorial.printfactorial,
        "type": "func"},
    2: {"display": "Prime Number Checker",
        "exec": prime.prime_print,
        "type": "func"},
    3: {"display": "Palindromes",
        "exec": palindrome.pal,
        "type": "func"}
}

mainMenu = {
    1: {"display":"Week 0",
        "exec": week0,
        "type": "submenu"},
    2: {"display":"Week 1",
        "exec": week1,
        "type": "submenu"},
    3: {"display":"Week 2",
        "exec": week2,
        "type": "submenu"},
    4: {"display":"Crossover Guessing Game",
        "exec": game.gamerun,
        "type": "func"}
}

if __name__ == "__main__":
    presentMenu(mainMenu)
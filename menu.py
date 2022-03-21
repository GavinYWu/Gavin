from week0.christmastree import christmastree
from week0.ship import ship
from week0.keypad import print_matrix
from week0.swap import swap
from week1.fibonacci import printFibonacci
from week1.infodb import for_loop,while_loop,recursive_loop
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
        "type":"func",
        "exec":op2}
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
        "type":"func"},
}

mainMenu = {
    1: {"display":"Christmas Tree",
        "exec":christmastree,
        "type":"func"},
    2: {"display":"Ship",
        "exec":ship,
        "type":"func"},
    3: {"display":"Keypad ",
        "exec":print_matrix,
        "type":"func"},
    4: {"display":"Swap ",
        "exec":swap,
        "type":"func"},
    5: {"display":"Submenu",
        "exec": subMenu,
        "type":"submenu"},
    6: {"display":"Finbonacci Sequence",
        "exec": printFibonacci,
        "type":"func"},
    7: {"display":"InfoDB",
        "exec": InfoDB,
        "type":"func"}
}

if __name__ == "__main__":
    presentMenu(mainMenu)
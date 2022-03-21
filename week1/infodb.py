# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "Name": "Gavin Wu",
    "Birthday": "April 6",
    "Residence": "San Diego",
    "Email": "gavinw24390@stu.powayusd.com",
    "Previous Schools":["Shanghai ShiYan Elementary School","D39C","MRES","OVMS", "DHS"]
})

InfoDb.append({
    "Name": "Karthik Valluri",
    "Birthday": "July 22",
    "Residence": "San Diego",
    "Email": "karthikv44293@stu.powayusd.com",
    "Previous Schools":["Dingeman Elementary School","Marshall Middle School","OVMS","DNHS"]
})

InfoDb.append({
    "Name": "Gilbert Puffington",
    "Birthday": "February 30",
    "Residence": "San Diego",
    "Email": "PuffingtonJR@gmail.com",
    "Previous Schools":["Elementary School A","Middle School B","High School C"]
})

# Hack 2
def print_data(x):
    print(InfoDb[x]["Name"])
    print("\t", "Birthday:", end="")
    print("\t", "Email: ", end="")
    print(", ".join(InfoDb[x]["Previous Schools"]))
    print()


def for_loop():
    for x in range(len(InfoDb)):
        print_data(x)

def while_loop(x):
    x = 0
    while x < len(InfoDb):
        print_data(x)
        x += 1
    return

def recursive_loop(x):
    if x < len(InfoDb):
        print_data(x)
        recursive_loop(x+1)
        return recursive_loop(x + 1)

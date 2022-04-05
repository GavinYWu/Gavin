---
title: Data Structures Projects
layout: template
filename: Data-Structures-Projects
--- 

## [Code Snippets](https://gavinywu.github.io/Gavin/codesnippets)

### Replit Code
<div class="row justify-content-center" style="margin: 2%;">
    <iframe height="1000px" width="700px" src="https://replit.com/@GavinWu3/Gavin?lite=true#menu.py"></iframe>
</div>  

### Code Snippets
```
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
})
```
This is a list of dictionaries which store the data
```
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
```
Functions to call the data

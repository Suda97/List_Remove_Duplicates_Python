import random


def delDupliUno(li):  # Using loop to make list without duplicates
    x = []
    for el in li:
        if el not in x:
            x.append(el)
    return x


def delDupliDuo(li):  # Using sets to make set without duplicates
    x = set(li)  # We can just change whole list to set and this will delete all duplicates
    return x  # Because sets aren't allowed to have duplicates


def task5():
    a = random.sample(range(0, 100), random.randint(1, 25))
    b = random.sample(range(0, 100), random.randint(1, 25))

    print(a)
    print(b)
    x = set(a).intersection(set(b))
    if len(x) > 0:
        return x
    else:
        return 'Empty set'


lis = []
i = random.randint(1, 30)  # Generating random length of the list

while i > 0:
    lis.append(random.randint(0, 5))  # Generating random list in range 0 - 5, add adding elements to the end of list
    i -= 1

print(lis)
print("Loop version result: ")
print(delDupliUno(lis))
print("Set version result: ")
print(delDupliDuo(lis))
print("Task number 5 using sets: ")
print(task5())

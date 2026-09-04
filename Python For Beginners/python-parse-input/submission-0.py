from typing import List

def read_integers() -> List[int]:
    line = input()
    strings = line.split(",")
    intlist = []

    for s in strings:
        intlist.append(int(s))

    return intlist

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

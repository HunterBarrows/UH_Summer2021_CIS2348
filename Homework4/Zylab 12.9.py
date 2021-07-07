# Hunter Barrows 1550107

# Zylab 12.9

# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]

# tries to run function and corrects to zero if 2nd input is not a interger
while name != '-1':
    try:
        age = int(parts[1]) + 1
    except ValueError:
        age = 0
    print('{} {}'.format(name, age))

    parts = input().split()
    name = parts[0]
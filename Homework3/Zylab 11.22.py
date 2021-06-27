# Hunter Barrows    1550107

# Zylab 11.22

# Gets input values and puts it into a list
val = input()
list_input = val.split(' ')

# creates for loop and counts the amount of time word appears in list
for i in list_input:
    frequency = list_input.count(i)
    print(i, frequency)

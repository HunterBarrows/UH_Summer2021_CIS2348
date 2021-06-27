# Hunter Barrows    1550107

# Zylab 11.18

# Gets input values and puts it into a list
val = input()
list_input = val.split(' ')

# Converts a list  into intergers
map_list = map(int, list_input)
list_num = list(map_list)

# creates a for loop and removes negatives
for item in list_num:
    if item < 0:
        list_num.remove(item)

# sorts items in list from smallest to largest
list_num.sort()

# double check items outputs positive numbers only and print numbers
for i in list_num:
    if i >= 0:
        print(i, end=' ')
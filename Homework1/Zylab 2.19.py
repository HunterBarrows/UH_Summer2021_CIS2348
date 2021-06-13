# Hunter Barrows 1550107

# Zylab 2.19 Cooking Measurement

# User prompt

juice = float(input('Enter amount of lemon juice (in cups):\n'))
water = float(input('Enter amount of water (in cups):\n'))
nectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))
print()
# list ingredients

print('Lemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(juice), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(nectar), 'cup(s) agave nectar')
print()

# Number of servings desired
qty_servings = float(input('How many servings would you like to make?\n'))
print()
print('Lemonade ingredients - yields', '{:.2f}'.format(qty_servings), 'servings')
juice1 = juice * (qty_servings / servings)
water1 = water * (qty_servings / servings)
nectar1 = nectar * (qty_servings / servings)

print('{:.2f}'.format(juice1), 'cup(s) lemon juice')
print('{:.2f}'.format(water1), 'cup(s) water')
print('{:.2f}'.format(nectar1), 'cup(s) agave nectar')
print()

juice2 = juice1 / 16
water2 = water1 / 16
nectar2 = nectar1 / 16

# Gallon Conversions
print('Lemonade ingredients - yields', '{:.2f}'.format(qty_servings), 'servings')
print('{:.2f}'.format(juice2), 'gallon(s) lemon juice')
print('{:.2f}'.format(water2), 'gallon(s) water')
print('{:.2f}'.format(nectar2), 'gallon(s) agave nectar')



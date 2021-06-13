# Hunter Barrows 1550107

# Zylab 3.19 Painting a Wall

# Prompt User

import math

Height = int(input('Enter wall height (feet):\n'))
Width = int(input('Enter wall width (feet):\n'))
Wall_Area = Height * Width

print('Wall area:', Wall_Area, 'square feet')


# Gallons of Paint Needed

Gallon = 350
paint_needed = Wall_Area / Gallon

print('Paint needed:', '{:.2f}'.format(paint_needed), 'gallons')


# Cans Needed

Gallon_Can = math.ceil(paint_needed)

print('Cans needed:', Gallon_Can, 'can(s)')
print()

# Color User Wants

color = {'red': 35, 'blue': 25, 'green': 23}

color_chosen = input('Choose a color to paint the wall:\n')
cans_needed = color[color_chosen] * Gallon_Can
print('Cost of purchasing', color_chosen, 'paint:', '{}{}'.format('$', cans_needed))

# Hunter Barrows 1550107

# Zylab 6.22 Brute Force Equation Solver

# Equation 1
a = int(input())
b = int(input())
c = int(input())

# Equation 2
d = int(input())
e = int(input())
f = int(input())

Fx = 100
Fy = 100

# For loop for equation
for x in range(-10, 11):
    for y in range(-10, 11):
        if (a * x + b * y == c) and (d * x + e * y == f):
            Fx = x
            Fy = y
            break

# Final print statement if there is a solution or no solution
if Fx != 100 or Fy != 100:
    print(Fx, Fy)
else:
    print('No solution')









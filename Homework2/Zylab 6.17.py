# Hunter Barrows 1550107

# Zylab 6.17 Password Modifier

# input value
user_word = input()
password = ''

# For loop for input
for chr in user_word:
    if chr == 'i':
        password += '!'
    elif chr == 'a':
        password += '@'
    elif chr == 'm':
        password += 'M'
    elif chr == 'B':
        password += '8'
    elif chr == 'o':
        password += '.'
    else:
        password += chr

# Append 'q*s' to password
password = password + 'q*s'
print(password)
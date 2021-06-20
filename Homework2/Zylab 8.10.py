# Hunter Barrows 1550107

# Zylab 8.10

# takes user input and removes spaces
user_input = str(input())
palindrome = user_input.lower().replace(" ","")

# test if word is palindrome
if palindrome[::1] == palindrome[::-1]:
    print(user_input, 'is a palindrome')
else:
    print(user_input, 'is not a palindrome')
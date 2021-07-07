# Hunter Barrows 1550107

# Zylab 12.7

# Gets user_age and checks if it is valid
def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    return age

# calculate heart_rate with user age
def fat_burning_heart_rate(age):
    heart_rate = .7 * (220-age)
    return heart_rate

# calls the functions and print the corresponding message
if __name__ == "__main__":
    try:
        age = get_age()
        fat_burning = fat_burning_heart_rate(age)

        print('Fat burning heart rate for a', age, 'year-old:', fat_burning, 'bpm')
    except ValueError as excpt:
        print(excpt)
        print("Could not calculate heart rate info.\n")


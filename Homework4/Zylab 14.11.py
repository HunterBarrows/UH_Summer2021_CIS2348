# Hunter Barrows 1550107

# Zylab 14.11

# nested for loops created to take input values and print the numbers in subquential order with the number of rows for the amount of input values that were split
def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        max_index = i
        for x in range(i + 1, len(numbers)):
            if numbers[x] > numbers[max_index]:
                max_index = x
        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]
        for y in numbers:
            print(y, end=' ')
        print()
    return numbers


if __name__ == "__main__":
    numbers = [int(y) for y in input().split()]
    selection_sort_descend_trace(numbers)
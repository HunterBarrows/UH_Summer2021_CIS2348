# Hunter Barrows 1550107

# Zylab 14.13


# Global variable
num_calls = 0


def partition(user_ids, i, k):
    lower = (i - 1)
    middle = (i + k) // 2
    point = user_ids[middle]
    user_ids[middle], user_ids[k] = user_ids[k], user_ids[middle]
    for x in range(i, k):
        if user_ids[x] <= point:
            lower += 1
            user_ids[lower], user_ids[x] = user_ids[x], user_ids[lower]
    user_ids[lower + 1], user_ids[k] = user_ids[k], user_ids[lower + 1]
    return (lower + 1)


def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1
    if i < k:
        index = partition(user_ids, i, k)
        quicksort(user_ids, i, index - 1)
        quicksort(user_ids, index + 1, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)


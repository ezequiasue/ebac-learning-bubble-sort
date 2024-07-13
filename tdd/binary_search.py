def binary_search(array, x, low, high):

    # Reapeat until the pointers low and high meet each other

    while low <= high:
        mid = low + (high - low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1



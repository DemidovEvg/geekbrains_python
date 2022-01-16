def binary_search(lst, number):
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = int((start + end) / 2)
        if lst[mid] == number:
            return True
        elif lst[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    return False
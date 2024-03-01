def improved_bubble_sort(arr):  # O(n^2)
    """
    Sort the list using bubble sort

    :param arr: to sort
    :return: None
    """
    n = len(arr)
    swapped = True
    while swapped:  # O(n^2)
        swapped = False
        for i in range(1, n):  # O(n)
            if arr[i - 1] > arr[i]:  # O(1)
                arr[i - 1], arr[i] = arr[i], arr[i - 1]  # O(1)
                swapped = True


def shell_sort(arr):  # O(n^2)
    """
    Sort a list using shell_sort

    :param arr: to sort
    :return: None
    """
    lenght = len(arr)
    interval = lenght // 2

    while interval > 0:
        for i in range(interval, lenght):
            insert_value = arr[i]
            insert_index = i

            while insert_index >= interval and arr[insert_index - interval] > insert_value:
                arr[insert_index] = arr[insert_index - interval]
                insert_index -= interval

            arr[insert_index] = insert_value
        interval //= 2


def longest_common_subsequence(sequencies):  # O(n^2)
    """
    Find the size of the biggest subsequence in to sequences.

    :param sequencies: array with the two sequences
    :param X: First sequence
    :param Y: Second sequence
    :return: Size
    """
    X = sequencies[0]
    Y = sequencies[1]
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):  # O(n^2)
        for j in range(n + 1):  # O(n)
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L[m][n]


def two_nums_in_list_sum_to_k(lst: list, k: float) -> bool:
    """
    Returns True if lst contains 2 numbers that sum to k, False otherwise

    Args:
        lst (list): lst containing numbers
        k (float): integer to sum to

    Returns:
        bool: True if lst contains 2 numbers that sum to k, False otherwise
    """
    start = 0
    end = len(lst) - 1

    lst.sort()

    while start < end:
        sum_ = lst[start] + lst[end]
        if sum_ == k:
            return True
        elif sum_ > k:
            end -= 1
        else:
            start += 1

    return False

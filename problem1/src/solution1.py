def two_nums_in_list_sum_to_k(lst: list, k: float) -> bool:
    """
    Returns True if lst contains 2 numbers that sum to k, False otherwise

    Args:
        lst (list): lst containing numbers
        k (float): integer to sum to

    Returns:
        bool: True if lst contains 2 numbers that sum to k, False otherwise
    """
    set_ = set()

    for num in lst:
        if (k - num) in set_:
            return True
        set_.add(num)

    return False

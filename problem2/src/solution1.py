def product(lst: list) -> int:
    """
    returns the product of all integers in the list

    Args:
        lst (list): a list of integers

    Returns:
        int: the product of all integers in the list
    """
    prod = 1

    for val in lst:
        prod *= val

    return prod


def list_of_products_of_other_indicies(lst: list) -> list:
    """
    returns a list where the value at each index is the product of the numbers
    at all other indiices

    Args:
        lst (list): list of integers

    Returns:
        list: a list where the value at each index is the product of all other
        indiices
    """
    zero_index = None

    for index, val in enumerate(lst):
        if val == 0:
            if zero_index is not None:
                return [0 for _ in lst]

            zero_index = index

    if zero_index is not None:
        prod = product(lst[:zero_index] + lst[zero_index + 1:])
        return [prod if val == 0 else 0 for val in lst]

    prod = product(lst)
    return [prod // val for val in lst]

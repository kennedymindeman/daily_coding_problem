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
    prefix = [1]
    for val in lst[:-1]:
        prefix.append(prefix[-1] * val)

    suffix = [1]
    for val in lst[:0:-1]:
        suffix.append(suffix[-1] * val)

    return [prefix[i] * suffix[-i - 1] for i in range(len(lst))]

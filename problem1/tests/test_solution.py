from src.solution1 import two_nums_in_list_sum_to_k as func1
from src.solution1 import two_nums_in_list_sum_to_k as func2

funcs = [func1, func2]


def test_given_example():
    """
    test the example given in the problem statement
    """
    for func in funcs:
        result = func([10, 15, 3, 7], 17)
        assert result is True


def test_empty_list():
    """
    test the output of the function when passed an empty list
    """
    for func in funcs:
        result = func([], 0)
        assert result is False


def test_size_1_list():
    """
    test the output when the size of the list is 1
    """
    for func in funcs:
        result = func([0], 0)
        assert result is False


def test_sum_to_zero():
    """
    test the case where the sum is 0 and 0 is in the list
    """
    for func in funcs:
        result = func([0, 0], 0)
        assert result is True


def test_sum_not_in_list():
    """
    test a case where the sum isn't in the list
    """
    for func in funcs:
        result = func([0, 1, 2, 3], 6)
        assert result is False


def test_all_pairs_sum_to_k():
    """
    tests a case where all the possible pairings sum to k
    """
    for func in funcs:
        result = func([1, 1, 1], 2)
        assert result is True


def test_if_k_is_double_the_center_number():
    """
    checks if the function will double count the center value
    """
    for func in funcs:
        result = func([2, 1, 2], 2)
        assert result is False


def test_negative_sum():
    """
    tests if the sum and corresponding opperands are negative
    """
    for func in funcs:
        result = func([-1, 0, -2], -3)
        assert result is True

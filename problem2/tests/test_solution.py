from src.solution2 import list_of_products_of_other_indicies


def test_empty_list():
    result = list_of_products_of_other_indicies([])
    assert result == []


def test_2_zeroes():
    result = list_of_products_of_other_indicies([0, 0])
    assert result == [0, 0]


def test_2_zeroes_and_a_non_zero_num():
    result = list_of_products_of_other_indicies([0, 0, 1])
    assert result == [0, 0, 0]


def test_only_one_0():
    result = list_of_products_of_other_indicies([0, 1])
    assert result == [1, 0]


def test_given_testcase_1():
    result = list_of_products_of_other_indicies([1, 2, 3, 4, 5])
    assert result == [120, 60, 40, 30, 24]


def test_given_testcase_2():
    result = list_of_products_of_other_indicies([3, 2, 1])
    assert result == [2, 3, 6]

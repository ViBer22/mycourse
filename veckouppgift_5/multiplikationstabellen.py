def test_multiplication_table():
    assert multiplication_table(3, 4) == [3, 6, 9, 12]
    assert multiplication_table(5, 0) == []
    assert multiplication_table(7, 3) == [7, 14, 21]
    assert multiplication_table(1, 5) == [1, 2, 3, 4, 5]


def multiplication_table(n, limit):
    return [n * i for i in range(1, limit + 1)]

test_multiplication_table()

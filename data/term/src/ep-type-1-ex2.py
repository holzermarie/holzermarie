def indices(element, entiers):
    ...


# tests

assert indices(3, [3, 2, 1, 3, 2, 1]) == [0, 3]
assert indices(4, [1, 2, 3]) == []
assert indices(1, [1, 1, 1, 1]) == [0, 1, 2, 3]
assert indices(5, [0, 0, 5]) == [2]
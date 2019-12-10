import itertools
import operator

data = [1, 2, 3, 4, 5]
max_data = [6, 7, 8, 4, 3, 6, 7, 4, 3, 6, 1]
numbers = ["one", "two", "three", "four"]


def accumulate(data):
    """Return sum of two close item"""
    return itertools.accumulate(data, operator.mul)


def max_accumulate(data):
    """Return the largest item"""
    return itertools.accumulate(data, max)


def no_accumulate(data):
    """If no function is designated the items will be summed."""
    return itertools.accumulate(data)


def combinator_func(data):
    """Create all the unique combination that have N members."""
    return itertools.combinations(data, 3)


def combinator_with_replacement_func(data):
    """Create all the combination that have N members."""
    return itertools.combinations_with_replacement(data, 2)


def count_func():
    """Makes an iterator that returns evenly spaced values starting with number start."""
    for i in itertools.count(start=20, step=2):
        print(i, end=" ")
        if i > 40:
            break


def show(iter_func):
    print(list(iter_func))


show(accumulate(data))
show(max_accumulate(max_data))
show(no_accumulate(data))
show(combinator_func(numbers))
show(combinator_with_replacement_func(numbers))
count_func()

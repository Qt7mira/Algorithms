a = [5, 3, 8, 5, 1, 9, 3, 0, 2, 8, 46, 2, 7, 4, 0, 2, 7]

b = sorted(a)
import random


def fast_sorted(L):
    if len(L) < 2:
        return L
    pivot_element = random.choice(L)
    small = [i for i in L if i < pivot_element]
    medium = [i for i in L if i == pivot_element]
    large = [i for i in L if i > pivot_element]
    return fast_sorted(small) + medium + fast_sorted(large)


print(fast_sorted(a))

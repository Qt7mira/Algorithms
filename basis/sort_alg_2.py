# -*- coding: utf-8 -*-

"""
Authors: qt7mira
Date:    2020/1/19
排序算法2
归并 & 快排
"""
import random


def merge_sort(array):
    """
    归并排序
    :param array:
    :return:
    """

    def merge(array_a, array_b):
        """
        merge
        :param array_a:
        :param array_b:
        :return:
        """
        result = []

        n1 = len(array_a)
        n2 = len(array_b)

        p, q = 0, 0
        while p < n1 and q < n2:

            if array_a[p] <= array_b[q]:
                result.append(array_a[p])
                p += 1
            else:
                result.append(array_b[q])
                q += 1

        result += array_a[p:]
        result += array_b[q:]

        return result

    def merge_sort_part(array):
        """
        sort part
        :param array:
        :return:
        """

        if len(array) <= 1:
            return array

        mid = len(array) // 2
        a = merge_sort_part(array[:mid])
        b = merge_sort_part(array[mid:])
        c = merge(a, b)
        return c

    return merge_sort_part(array)


def quick_sort(array, l, r):
    """
    稳定（原地）排序
    :param array:
    :return:
    """

    def partition(array, l, r):
        """
        partition
        :param array:
        :param l:
        :param r:
        :return:
        """

        pivot = array[r]
        i = l

        for j in range(l, r):
            if array[j] <= pivot:

                array[i], array[j] = array[j], array[i]
                i += 1

        array[i], array[r] = array[r], array[i]
        return i

    if l < r:
        pivot = partition(array, l, r)

        quick_sort(array, l, pivot - 1)
        quick_sort(array, pivot + 1, r)


def quick_sort_2(array):
    """
    不稳定（非原地）排序
    :param array:
    :return:
    """

    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    low = [i for i in array if i < pivot]
    high = [i for i in array if i > pivot]
    middle = [i for i in array if i == pivot]
    return quick_sort_2(low) + middle + quick_sort_2(high)


if __name__ == '__main__':

    array_1 = [5, 6, -1, 4, 2, 8, 10, 7, 3]
    print(merge_sort(array_1))

    print(quick_sort_2(array_1))

    quick_sort(array_1, 0, len(array_1) - 1)
    print(array_1)

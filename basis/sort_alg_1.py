# -*- coding: utf-8 -*-
"""
Authors: panqiutong
Date:    2019/12/18
排序算法1
冒泡，插入，选择
"""
import random
import time
import unittest


def bubble_sort(array):
    """
    冒泡排序
    :param array:
    :return:
    """
    length = len(array)
    if length <= 1:
        return
    for i in range(length):
        flag = False
        for j in range(length - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if not flag:
            break


def insertion_sort(array):
    """
    插入排序
    :param array:
    :return:
    """
    length = len(array)
    if length <= 1:
        return
    for i in range(1, length):
        value = array[i]
        for j in (reversed(range(i))):
            if value < array[j]:
                array[j + 1] = array[j]
            else:
                break
            array[j] = value


def selection_sort(array):
    """
    选择排序
    :param array:
    :return:
    """
    length = len(array)
    if length <= 1:
        return
    for i in range(length):
        min_idx = i
        for j in range(i + 1, length):
            if array[min_idx] > array[j]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]


class TestDict(unittest.TestCase):
    """
    unit test class
    """

    def test_sort(self):
        """
        test_sort
        :return:
        """
        array_a = [5, 6, -1, 4, 2, 8, 10, 7, 6]
        array_b, array_c = array_a, array_a
        bubble_sort(array_a)
        assert array_a == [-1, 2, 4, 5, 6, 6, 7, 8, 10]

        insertion_sort(array_b)
        assert array_b == [-1, 2, 4, 5, 6, 6, 7, 8, 10]

        selection_sort(array_c)
        assert array_c == [-1, 2, 4, 5, 6, 6, 7, 8, 10]


def performance_comparison(n):
    """
    性能比较
    :param n:
    :return:
    """
    random_list_a, random_list_b, random_list_c = [], [], []
    for i in range(n):
        random_list_a.append(random.randint(-1000, 1000))
        random_list_b.append(random.randint(-1000, 1000))
        random_list_c.append(random.randint(-1000, 1000))

    tp_0 = int(time.time() * 1000)
    print(random_list_a[0:10])
    bubble_sort(random_list_a)
    print(random_list_a[0:10])
    tp_1 = int(time.time() * 1000)
    print("冒泡排序排序随机{}元素的队列用时 {} ms \n".format(n, tp_1 - tp_0))

    tp_0 = int(time.time() * 1000)
    print(random_list_b[0:10])
    insertion_sort(random_list_b)
    print(random_list_b[0:10])
    tp_1 = int(time.time() * 1000)
    print("插入排序排序随机{}元素的队列用时 {} ms \n".format(n, tp_1 - tp_0))

    tp_0 = int(time.time() * 1000)
    print(random_list_c[0:10])
    selection_sort(random_list_c)
    print(random_list_c[0:10])
    tp_1 = int(time.time() * 1000)
    print("选择排序排序随机{}元素的队列用时 {} ms \n".format(n, tp_1 - tp_0))


if __name__ == '__main__':

    # # 单元测试
    # unittest.main()

    performance_comparison(10000)

    array_1 = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    bubble_sort(array_1)
    print(array_1)

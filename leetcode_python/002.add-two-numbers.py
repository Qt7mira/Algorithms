#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (31.35%)
# Likes:    5469
# Dislikes: 1405
# Total Accepted:    924.2K
# Total Submissions: 2.9M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        result = ListNode(0)

        p = l1
        q = l2
        current = result
        carry = 0

        while p is not None or q is not None:

            x = p.val if p is not None else 0
            y = q.val if q is not None else 0

            sum = x + y + carry
            carry = sum // 10
            sum = sum % 10

            current.next = ListNode(sum)
            current = current.next

            if p is not None:
                p = p.next
            if q is not None:
                q = q.next

        if carry > 0:
            current.next = ListNode(carry)

        return result.next

#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (56.63%)
# Likes:    584
# Dislikes: 0
# Total Accepted:    100.1K
# Total Submissions: 176.6K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy = ListNode(0)
        curr = dummy

        p = l1
        q = l2

        while p is not None or q is not None:
            x = p.val if p is not None else None
            y = q.val if q is not None else None

            if x is None and y is not None:
                curr.next = ListNode(y)
                q = q.next
            elif x is not None and y is None:
                curr.next = ListNode(x)
                p = p.next
            else:
                if x <= y:
                    curr.next = ListNode(x)
                    p = p.next
                else:
                    curr.next = ListNode(y)
                    q = q.next

            curr = curr.next

        return dummy.next




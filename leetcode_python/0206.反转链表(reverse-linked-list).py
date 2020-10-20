#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (63.79%)
# Likes:    595
# Dislikes: 0
# Total Accepted:    103.5K
# Total Submissions: 160K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None

        while head:
            # 备份head.next
            tmp = head.next

            # head.next指向新head的头结点
            head.next = new_head

            # 移动新head到目前的头结点
            new_head = head

            # head移动到下一个节点，即刚才备份好的tmp
            head = tmp

        return new_head


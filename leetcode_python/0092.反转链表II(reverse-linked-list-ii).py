#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (46.24%)
# Likes:    185
# Dislikes: 0
# Total Accepted:    17.4K
# Total Submissions: 37.5K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        """
              pre_head  mod_list_tail     mod_list_head  tail
        换序前：   1         2         3         4         5
        换序后：   1         4         3         2         1

        pre_head.next = mod_list_head
        mod_list_tail.next = tail
        """

        # 不换序的步数
        pre_len = m - 1

        # 换序步数
        change_len = n - m + 1

        # 备份头结点
        result = head
        new_head = None
        pre_head = None

        # 备份pre_head，他将指向mod_list_head
        while head and pre_len:
            pre_head = head
            head = head.next
            pre_len -= 1

        # 备份mod_list_tail，他将指向tail
        modify_list_tail = head

        while head and change_len:
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
            change_len -= 1

        # mod_list_tail.next = tail
        modify_list_tail.next = head

        # 若有pre_head，意味着m>1
        # pre_head.next = mod_list_head
        if pre_head:
            pre_head.next = new_head
        else:
            # m=1
            result = new_head

        return result



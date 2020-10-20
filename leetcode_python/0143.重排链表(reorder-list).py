#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (56.31%)
# Likes:    329
# Dislikes: 0
# Total Accepted:    41.2K
# Total Submissions: 72.8K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
#
# 示例 2:
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head

        def find_mid(head):
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse_link_list(head):
            new_head = None
            while head:
                temp = head.next
                head.next = new_head
                new_head = head
                head = temp
            return new_head

        mid = find_mid(head)
        new_head = mid.next
        mid.next = None
        new_head = reverse_link_list(new_head)

        while new_head:
            # head 1 2 3
            # new_head 5 4
            temp = new_head.next
            new_head.next = head.next
            head.next = new_head
            head = new_head.next
            new_head = temp

        return

    # @lc code=end


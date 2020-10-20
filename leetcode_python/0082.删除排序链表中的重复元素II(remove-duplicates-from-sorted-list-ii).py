#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (43.13%)
# Likes:    150
# Dislikes: 0
# Total Accepted:    20.1K
# Total Submissions: 45.7K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#
#
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        # 应该还有更好的办法……

        dummy, pre = ListNode(None), ListNode(None)
        pre.next = head
        curr = dummy

        while head and head.next:
            if head.next and head.val != head.next.val and head.val != pre.val:
                curr.next = head
                curr = curr.next
            head = head.next
            pre = pre.next

        if head and head.val != pre.val:
            curr.next = head
        else:
            curr.next = None

        return dummy.next

# @lc code=end


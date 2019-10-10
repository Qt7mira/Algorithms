#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (38.98%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    22.8K
# Total Submissions: 58.4K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
#
#
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        curr = head
        len = 0
        while curr is not None:
            len += 1
            curr = curr.next

        if len <= 1:
            return head

        k = k % len

        if k == 0:
            return head

        k = len - k

        curr = head
        while k - 1:
            curr = curr.next
            k -= 1

        tmp, new_head = curr.next, curr.next
        curr.next = None

        while tmp.next is not None:
            tmp = tmp.next

        tmp.next = head

        return new_head

# @lc code=end


#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (53.88%)
# Likes:    275
# Dislikes: 0
# Total Accepted:    23.2K
# Total Submissions: 42.5K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 示例 :
#
# 给定这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
# 说明 :
#
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        dummy = ListNode(0)
        curr = dummy

        while True:
            tmp = head
            stack = []
            count = k
            while tmp and count:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1

            # 多出的不够k个的链表节点
            if count:
                curr.next = head
                # 跳出，返回结果
                break

            while stack:
                curr.next = stack.pop()
                curr = curr.next

            # 反转完了把剩下的连起来
            curr.next = tmp
            head = tmp

        return dummy.next

# @lc code=end


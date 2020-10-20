#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (47.39%)
# Likes:    316
# Dislikes: 0
# Total Accepted:    37.9K
# Total Submissions: 80K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if lists is None or len(lists) == 0:
            return None

        def list_sort(lists, l, r):
            if l >= r:
                return lists[l]
            mid = (r - l) // 2 + l
            l1 = list_sort(lists, l, mid)
            l2 = list_sort(lists, mid + 1, r)
            return merge(l1, l2)

        def merge(l1, l2):
            dummy = ListNode(0)
            curr = dummy

            p = l1
            q = l2

            while p is not None or q is not None:
                x = p.val if p is not None else None
                y = q.val if q is not None else None

                if x is not None and y is None:
                    curr.next = ListNode(x)
                    p = p.next

                elif x is None and y is not None:
                    curr.next = ListNode(y)
                    q = q.next

                else:
                    if x <= y:
                        curr.next = ListNode(x)
                        p = p.next
                    else:
                        curr.next = ListNode(y)
                        q = q.next

                curr = curr.next
            return dummy.next

        return list_sort(lists, 0, len(lists) - 1)



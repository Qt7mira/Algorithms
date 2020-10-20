# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 思路，相当于补齐两链表      交
        # 1 2 3 4   ->   1 2 3 4 7 3 4
        # 7 3 4     ->   7 3 4 1 2 3 4

        ha, hb = headA, headB

        # 终止条件：要么相等，要么都遍历完（None = None）
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA

        return ha

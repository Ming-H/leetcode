#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        last_sorted = head
        cur = head.next
        while cur:
            if cur.val >= last_sorted.val:
                last_sorted = last_sorted.next
            else:
                pre = dummy
                while pre.next.val < cur.val:
                    pre = pre.next
                last_sorted.next = cur.next
                cur.next = pre.next
                pre.next = cur
            cur = last_sorted.next
        return dummy.next







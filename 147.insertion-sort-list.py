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
        p = dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val:
                cur = cur.next
                continue
            if p.next.val > val:
                p = dummy
            while p.next.val < val:
                p = p.next
            new = cur.next
            cur.next = new.next
            new.next = p.next
            p.next = new
        return dummy.next






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
        curr = head.next
        last_sorted = head
        while curr:
            if curr.val >= last_sorted.val:
                last_sorted = last_sorted.next
            else:
                prev = dummy
                while prev.next.val < curr.val:
                    prev = prev.next
                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = last_sorted.next
        return dummy.next







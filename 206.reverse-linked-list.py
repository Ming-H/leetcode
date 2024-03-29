#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre



    


#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        pre = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            pre, pre.next, slow = slow, pre, slow.next
        if fast:
            slow = slow.next
        while pre and pre.val == slow.val:
            slow = slow.next
            pre = pre.next
        return not pre




        


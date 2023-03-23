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
        if not head or not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            slow  = slow.next
            fast = fast.next.next
        pre = None
        while slow:
            cur = slow
            slow = slow.next
            cur.next = pre
            pre = cur
        while pre:
            if pre.val!=head.val:
                return False
            pre = pre.next
            head = head.next
        return True    


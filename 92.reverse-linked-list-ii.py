#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if not head:
            return None
        pre, cur  = None, head
        while m>1:
            pre = cur
            cur = cur.next
            m, n = m-1, n-1
        con, tail = pre, cur
        while n:
            third = cur.next
            cur.next = pre
            pre = cur
            cur = third
            n -= 1
        if con:
            con.next = pre
        else:
            head = pre
        tail.next = cur
        return head



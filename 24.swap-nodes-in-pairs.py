#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # pre, pre.next = self, head
        # while pre.next and pre.next.next:
        #     a, b = pre.next, pre.next.next
        #     pre.next, b.next, a.next = b, a, b.next
        #     pre = a
        # return self.next
        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy
        while ptr.next and ptr.next.next:
            a, b = ptr.next, ptr.next.next
            ptr.next, b.next, a.next = b, a, b.next 
            ptr = a
        return dummy.next 
                    


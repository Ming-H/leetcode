#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
            
        p = head
        length = 1
        while p.next:
            p = p.next
            length += 1
        rotateTimes = int(k%length)
        if k == 0 or rotateTimes == 0:
            return head
        
        fast, slow = head, head 
        for i in range(rotateTimes):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        temp = slow.next
        slow.next = None
        fast.next = head
   
        
        return temp


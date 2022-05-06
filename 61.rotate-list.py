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
    
        if head.next == None:
            return head
            
        pointer = head
        length = 1
        
        while pointer.next:
            pointer = pointer.next
            length += 1
        
        rotateTimes = int(k%length)
        
        if k == 0 or rotateTimes == 0:
            return head
        
        fastPointer = head
        slowPointer = head
        
        for i in range(rotateTimes):
            fastPointer = fastPointer.next
        
        
        while fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
        
        temp = slowPointer.next
        
        slowPointer.next = None
        fastPointer.next = head
        head = temp
        
        return head


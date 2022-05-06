#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = n2 = ''
        
        while l1 != None:
            n1 += str(l1.val)
            l1 = l1.next
        
        while l2 != None:
            n2 += str(l2.val)
            l2 = l2.next
            
        n3 = str(int(n1) + int(n2))
        
        head = ListNode(int(n3[0]))
        res = head
        for i in range(1,len(n3)):
            head.next = ListNode(int(n3[i]))
            head = head.next
            
        return res


# @lc code=end


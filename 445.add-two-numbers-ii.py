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
        s1,s2=0,0
        while l1:
            s1=s1*10+l1.val
            l1=l1.next
        while l2:
            s2=s2*10+l2.val
            l2=l2.next
        head=dummy=ListNode(0)
        for item in str(s1+s2):
            dummy.next = ListNode(item)
            dummy = dummy.next 
        return head.next



# @lc code=end


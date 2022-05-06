#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
         O(1) extra space 
         takes O(n) time.
        """
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
        
# @lc code=end


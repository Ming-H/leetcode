#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        注意：
        在奇偶组内，各数字要保持原来的顺序
        第一个是奇数，第二个是偶数
        """
        if not head : 
            return head
        odd = oddHead = head
        even = evenHead = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return oddHead





# @lc code=end


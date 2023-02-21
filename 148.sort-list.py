#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    https://www.cnblogs.com/grandyang/p/4249905.html
    归并排序
    用快慢指针确定中间元素，拆分左右两部分，之后递归合并
    """
    def sortList(self, head):
        if not head or not head.next:
            return head
        slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, left, right):
        res = cur = ListNode(0)
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
                cur = cur.next
            else:
                cur.next = right
                right = right.next
                cur = cur.next
        if left:
            cur.next = left
        if right:
            cur.next = right
        return res.next



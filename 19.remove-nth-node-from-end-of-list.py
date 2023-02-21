#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        需要用两个指针来帮助我们解题，pre 和 cur 指针。
        首先 cur 指针先向前走N步，如果此时 cur 指向空，说明N为链表的长度，
        则需要移除的为首元素，那么此时返回 head->next 即可，
        如果 cur 存在，再继续往下走，此时 pre 指针也跟着走，
        直到 cur 为最后一个元素时停止，此时 pre 指向要移除元素的前一个元素，
        我们再修改指针跳过需要移除的元素即可
        """
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next #删除第一个元素
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head # 返回头
        

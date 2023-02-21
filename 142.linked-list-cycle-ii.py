#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Definition for singly-linked list.
        # 参考287
        """
        因为快指针每次走2，慢指针每次走1，快指针走的距离是慢指针的两倍。
        而快指针又比慢指针多走了一圈。所以 head 到环的起点+环的起点到
        他们相遇的点的距离 与 环一圈的距离相等。现在重新开始，head 运
        行到环起点 和 相遇点到环起点 的距离也是相等的，相当于他们同时减
        掉了 环的起点到他们相遇的点的距离
        """
        dummy=ListNode(0)
        dummy.next=head
        slow=fast=dummy
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                fast=dummy
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow 
        return  None    
      

# @lc code=end


#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        """
        1)计算链表长度length
        2）通过length、k判断每个子链表的长度
        3）再次遍历链表，切分并返回结果
        Time Complexity: O(N+k)
        Space Complexity: O(k)
        """
        cur = head
        N = 0
        while cur:
            N += 1
            cur = cur.next 
        width, remainder = divmod(N, k)

        res = []
        cur = head
        for i in range(k):
            per_head = cur
            for j in range(width + (i < remainder) - 1):
                if cur: 
                    cur = cur.next
            if cur:
                cur.next, cur = None, cur.next # 不可互换
            res.append(per_head)
        return res


# @lc code=end


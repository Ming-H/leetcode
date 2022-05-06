#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        dummy = Node(0, None, None, None)
        cur = dummy
        head = root

        while root:
            if root.left:
                cur.next = root.left
                cur = cur.next
            if root.right:
                cur.next = root.right
                cur = cur.next
            root = root.next
            if not root:
                cur = dummy
                root = dummy.next
                dummy.next = None
        return head

       


# @lc code=end


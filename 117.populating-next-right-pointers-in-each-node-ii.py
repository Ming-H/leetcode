#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start

# Definition for a Node.


from this import d


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """
        cur = root
        head, pre = None, None 
        while cur:
            if cur.left:
                if pre:
                    pre.next = cur.left 
                else:
                    head = cur.left 
                pre = cur.left 
            if cur.right:
                if pre:
                    pre.next = cur.right 
                else:
                    head =  cur.right 
                pre = cur.right 
            cur = cur.next 
            if not cur:
                cur = head 
                pre, head = None, None 
        return root 












# @lc code=end


#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        由于是完全二叉树，所以若节点的左子结点存在的话，
        其右子节点必定存在，所以左子结点的 next 指针可
        以直接指向其右子节点，对于其右子节点的处理方法是，
        判断其父节点的 next 是否为空，若不为空，则指向
        其 next 指针指向的节点的左子结点，若为空则指向 NULL
        """
        if root and root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None
            self.connect(root.left)
            self.connect(root.right)
        return root
        """
        用两个指针 start 和 cur，其中 start 标记每一层的起始节点，
        cur 用来遍历该层的节点
        """
        # if not root:
        #     return None
        # start = root
        # cur = None
        # while start.left:
        #     cur = start
        #     while cur:
        #         cur.left.next = cur.right
        #         if cur.next:
        #             cur.right.next = cur.next.left
        #         cur = cur.next
        #     start = start.left
        # return root



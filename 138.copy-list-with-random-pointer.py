#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        nodeDict = dict()
        dummy = Node(0, None, None)
        nodeDict[head] = dummy
        newHead, pointer = dummy, head
        while pointer:
            node = Node(pointer.val, pointer.next, None)
            nodeDict[pointer] = node
            newHead.next = node
            newHead, pointer = newHead.next, pointer.next
        pointer = head
        while pointer:
            if pointer.random:
                nodeDict[pointer].random = nodeDict[pointer.random]
            pointer = pointer.next
        return dummy.next

        
# @lc code=end


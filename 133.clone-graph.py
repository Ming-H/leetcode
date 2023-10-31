#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution:
    #  bfs
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        m, visited, queue = {}, set(), collections.deque([node])
        while queue:
            n = queue.popleft()
            if n in visited:
                continue
            visited.add(n)
            if n not in m:
                m[n] = Node(n.val)
            for neigh in n.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
                queue.append(neigh)
        return m[node]

    # dfs iteratively
    def cloneGraph1(self, node):
        if not node:
            return node
        m, visited, stack = dict(), set(), deque([node])
        while stack:
            n = stack.pop()
            if n in visited:
                continue
            visited.add(n)
            if n not in m:
                m[n] = Node(n.val)
            for neigh in n.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
                stack.append(neigh)
        return m[node]

        # dfs recursively
    def cloneGraph2(self, node):
        if not node:
            return node
        m, visited = dict(), set()
        self.dfs(node, m, visited)
        return m[node]

    def dfs(self, n, m, visited):
        if n in visited:
            return
        visited.add(n)
        if n not in m:
            m[n] = Node(n.val)
        for neigh in n.neighbors:
            if neigh not in m:
                m[neigh] = Node(neigh.val)
            m[n].neighbors.append(m[neigh])
            self.dfs(neigh, m, visited)

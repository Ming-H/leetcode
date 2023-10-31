#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        First, we need to build a graph using the given equations and values. 
        Each variable will be represented as a node in the graph, and the values 
        will be the weights of the edges between the nodes.
        """
        # Build the graph
        graph = defaultdict(dict)
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value

        def dfs(a, b, visited):
            # If either a or b is undefined, return -1.0
            if a not in graph or b not in graph:
                return -1.0
            # If we reach the b node, return the res
            if a == b:
                return 1.0
            visited.add(a)
            # Traverse the graph using DFS
            for neighbor, value in graph[a].items():
                if neighbor not in visited:
                    res = dfs(neighbor, b, visited)
                    if res != -1.0:
                        return value * res
            return -1.0

        # Evaluate each query
        res = []
        for a, b in queries:
            res.append(dfs(a, b, set()))
        return res
# @lc code=end

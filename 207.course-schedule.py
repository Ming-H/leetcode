#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        import collections
        # Prepare the graph
        adj_list = collections.defaultdict(list)
        indegree = {}
        
        for i, item in prerequisites:
            adj_list[item].append(i) # 保存依赖关系，后一个依赖于哪一些
            # Record each node's in-degree
            indegree[i] = indegree.get(i, 0) + 1

        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = [k for k in range(numCourses) if k not in indegree]

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:

            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.pop(0)
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return  len(topological_sorted_order) == numCourses 



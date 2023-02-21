#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
class Solution:
    def canFinish(self, n: int, nums: List[List[int]]) -> bool:
        import collections 
        d = collections.defaultdict(list) #记录当前学完，可以学的课程
        indegree = {}
        for a, b in nums:
            d[b].append(a)
            indegree[a] = indegree.get(a, 0) + 1
        zero_indegree = [k for k in range(n) if k not in indegree]
        res = []
        while zero_indegree:
            vertex = zero_indegree.pop(0)
            res.append(vertex)
            if vertex in d:
                for item in d[vertex]:
                    indegree[item] -= 1
                    if indegree[item] == 0:
                        zero_indegree.append(item)
        return len(res)==n






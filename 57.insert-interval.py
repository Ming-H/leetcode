#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval[0], newInterval[-1]
        left = []
        right = []
        for item in intervals:
            if item[-1]<s:
                left.append(item)
            elif item[0]>e:
                right.append(item)
            else:
                s = min(s, item[0])
                e = max(e, item[-1])
        return left + [[s, e]] + right



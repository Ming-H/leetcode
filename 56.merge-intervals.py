#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
class Solution:
    def merge(self, intervals):
        """
        Time complexity : O(nlogn)
        Space complexity : O(1) or O(n)
        """
        intervals.sort(key=lambda x: x[0])

        merged = []
        for item in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][-1] < item[0]:
                merged.append(item)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][-1] = max(merged[-1][-1], item[-1])

        return merged
    
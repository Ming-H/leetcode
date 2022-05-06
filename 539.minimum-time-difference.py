#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#

# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        total = 60*24
        buckets = [False]*total
        for time in timePoints:
            h, m = time.split(":")
            tm = int(h)*60+ int(m)
            if not buckets[tm]:
                buckets[tm] = True
            else:
                return 0
        #now iterate over the buckets
        prev = first = -1
        mn = total
        for i in range(total):
            if buckets[i]:
                if prev != -1:
                    mn = min(mn, i - prev)
                else:
                    first = i
                prev = i
        mn = min(mn, total - prev + first)  
        #first time and last time diff, e.g 0 and 1200, 1439, 
        # so here min is between 1439 and 0
        return mn

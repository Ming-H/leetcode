#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        max_freq = max(freq.values())
        freq = list(freq.values())
        cnt = 0                 
        i = 0
        while( i < len(freq)):
            if freq[i] == max_freq:
                cnt += 1
            i += 1
        res = (max_freq - 1) * (n+1) + cnt
        return max(res, len(tasks))


        # @lc code=end


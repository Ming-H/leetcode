#
# @lc app=leetcode id=1695 lang=python3
#
# [1695] Maximum Erasure Value
#

# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prefix = [0]
        for i in range(len(nums)):
            prefix += [prefix[-1] + nums[i]]

        lastpos = {}
        maxsum = 0
        left = 0
        for i, n in enumerate(nums):
            if n in lastpos:
                left = max(left, lastpos[n])
            lastpos[n] = i+1
            maxsum = max(maxsum, prefix[i+1] - prefix[left])

        return maxsum
        
# @lc code=end


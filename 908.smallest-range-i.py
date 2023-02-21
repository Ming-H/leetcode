#
# @lc app=leetcode id=908 lang=python3
#
# [908] Smallest Range I
#

# @lc code=start
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        M, m = max(nums), min(nums)
        diff, extension = M - m, 2*k
        
        if diff <= extension:
            return 0
        
        else:
            return diff - extension
# @lc code=end


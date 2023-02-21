#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        res = cur = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]:
                cur = i
            res = max(res, i-cur+1)
        return res 

        
# @lc code=end


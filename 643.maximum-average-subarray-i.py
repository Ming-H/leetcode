#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        Sum=0
        for i in range(k):
            Sum += nums[i]
        res = Sum
        for i in range(k, len(nums)):
            Sum += nums[i] - nums[i-k]
            res = max(res, Sum)
        return res / k
# @lc code=end


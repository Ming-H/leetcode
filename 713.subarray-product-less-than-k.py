#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        快慢指针
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if k<=1:
            return 0 
        prod = 1
        res, left = 0, 0
        for right, val in enumerate(nums):
            prod *= val 
            while prod >= k:
                prod /= nums[left]
                left += 1
            res += right-left +1
        return res 
    






# @lc code=end


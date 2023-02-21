#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        m = max(nums)
        if all(m >= 2*x for x in nums if x != m):
            return nums.index(m)
        return -1  

# @lc code=end


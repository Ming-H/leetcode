#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#

# @lc code=start
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = int((lo + hi) / 2)
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo

# @lc code=end


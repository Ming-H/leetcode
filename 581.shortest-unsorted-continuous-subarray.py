#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=i
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, n - 1
        while i < n - 1 and nums[i] <= nums[i+1]:
            i += 1
        if i == n - 1:
            return 0
        while j > 0 and nums[j] >= nums[j-1]:
            j -= 1
        Max = max(nums[i:j+1])
        Min = min(nums[i:j+1])
        while i > 0 and nums[i-1] > Min:
            i -= 1   
        while j < n-1 and nums[j+1] < Max:
            j += 1
        return j - i + 1




# @lc code=end


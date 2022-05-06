#
# @lc app=leetcode id=689 lang=python3
#
# [689] Maximum Sum of 3 Non-Overlapping Subarrays
#

# @lc code=start
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        """
        Time Complexity: O(N)
        Space complexity: O(N)
        """
        
        W = [] #array of sums of windows
        sum_ = 0
        for i, x in enumerate(nums):
            sum_ += x
            if i >= k: sum_ -= nums[i-k]
            if i >= k-1: W.append(sum_)

        left = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            left[i] = best

        right = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]:
                best = i
            right[i] = best

        ans = None
        for j in range(k, len(W) - k):
            i, k = left[j-k], right[j+k]
            if ans is None or (W[i] + W[j] + W[k] > W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = i, j, k
        return ans
        
# @lc code=end


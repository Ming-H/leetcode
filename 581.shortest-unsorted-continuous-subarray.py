#
# @lc app=leetcode id=581 lang=python3
#
# [581] Shortest Unsorted Continuous Subarray
#

# @lc code=start
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        https://www.cnblogs.com/jimmycheng/p/7673733.html
        Time complexity : O(n)
        Space complexity : O(1)
        """
        if len(nums)<2:
            return 0
        
        Min = float('inf')
        Max = float('-inf')
            
        # 对每一个逆序对计算最大、最小值
        for i in range(1, len(nums)):
        	if nums[i] < nums[i-1]:
        		Min = min(Min, nums[i])
        for l in range(len(nums)):
        	if Min < nums[l]:
        		break

        for i in range(len(nums)-2, -1, -1):
        	if nums[i]>nums[i+1]:
        		Max = max(Max, nums[i])
        for r in range(len(nums)-1, -1, -1):
        	if Max > nums[r]:
        		break

        if r-l<0:
        	return 0
        else:
        	return r-l+1

        # start, end = -1, -2
        # Min, Max = nums[-1], nums[0]

        # for i in range(len(nums)):
        #     Max = max(Max, nums[i])
        #     Min = min(Min, nums[len(nums)-i-1])
        #     if nums[i] < Max:
        #         end = i
        #     if nums[len(nums)-i-1] > Min:
        #         start = len(nums)-i-1
        # return end - start + 1






# @lc code=end


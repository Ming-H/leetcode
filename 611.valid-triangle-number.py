#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#

# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        Time complexity : O(n^2)
        Space complexity : O(logn)
        """
        count = 0
        nums.sort()
        for i in range(0, len(nums)-2):
            k = i+2
            if nums[i]!=0:
                for j in range(i+1, len(nums)-1):
                    while k<len(nums) and \
                            nums[i]+nums[j]>nums[k]:
                        k += 1
                    count += k-j-1 #(k−1)−(j+1)+1=k−j−1.
        return count

# @lc code=end


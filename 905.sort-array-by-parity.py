#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        i, j = 0, len(nums)-1
        while i<j:
            if nums[i]%2>nums[j]%2:
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i]%2==0:
                i += 1
            if nums[j]%2==1:
                j -= 1
        return nums 

# @lc code=end


#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for item in nums:
            a = abs(item) - 1
            if nums[a] > 0: 
                nums[a] *= -1
        res = [i+1 for i in range(len(nums)) if nums[i] > 0]
        return res

        
# @lc code=end


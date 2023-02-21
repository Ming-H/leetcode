#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#

# @lc code=start
from matplotlib.colors import cnames


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """
        Time Complexity:O(N).
        space complexity is O(1)
        """
        count = 0 
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]: 
                count += 1
                if count > 1: 
                    return False
                # if-else: only can modify one value out of the (i, i+1) pair
                if i == 0 or nums[i-1] <= nums[i+1]: 
                    # ex: 1 4 3
                    #       ^ 
                    #       i
                    # since lhs = 1 & rhs = 3 and lhs <= rhs, modify i = 3
                    # result: 1 3 3
                    nums[i] = nums[i+1]
                else: 
                    # ex: 3 4 2
                    #       ^
                    #       i
                    # since lhs = 3 & rhs = 2 and lhs > rhs, modify i+1 = 4
                    # result: 3 4 4
                    nums[i+1] = nums[i]
        return count <= 1
   



# @lc code=end


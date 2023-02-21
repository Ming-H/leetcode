#
# @lc app=leetcode id=565 lang=python3
#
# [565] Array Nesting
#

# @lc code=start
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        res = 0
        for item in nums:
            if item != float('inf'):
                start = item
                count = 0
                while nums[start]!=float('inf'):
                    nums[start], start = float('inf'), nums[start]
                    count += 1
                res = max(res, count)
        return res



                


# @lc code=end


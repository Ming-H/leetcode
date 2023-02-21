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
        nums.sort()
        res = 0
        for index_i in range(len(nums)-1, 1, -1):
            third_edge = nums[index_i]
            index_first, index_second = 0, index_i - 1
            while index_first < index_second:
                first_edge = nums[index_first]
                second_edge = nums[index_second]
                if first_edge + second_edge > third_edge:
                    res += index_second - index_first
                    index_second -= 1
                else:
                    index_first += 1
        return res





    

# @lc code=end


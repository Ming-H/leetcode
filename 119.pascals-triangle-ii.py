#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, n: int) -> List[int]:
        nums = [1] * (n+1)
        for i in range(2, n+1):
            for j in range(i-1, 0, -1):
                nums[j] += nums[j-1]
        return nums

# @lc code=end


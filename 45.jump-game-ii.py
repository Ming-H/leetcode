#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max_reach, step, end = 0, 0, 0
        for i in range(len(nums)-1):
            max_reach = max(max_reach, i+nums[i])
            if i == end:
                end = max_reach
                step += 1
            if end >= len(nums)-1:
                return step
        return False


# @lc code=end

#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        start, end, step = 0, 0, 0
        while end < len(nums) - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= len(nums) - 1:  # 等号
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step

# @lc code=end


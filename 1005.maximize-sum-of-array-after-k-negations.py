#
# @lc app=leetcode id=1005 lang=python3
#
# [1005] Maximize Sum Of Array After K Negations
#

# @lc code=start

import heapq

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while i < len(nums) and i < k and nums[i] < 0:
            nums[i] = -nums[i]
            i += 1
        # 翻转最小值并从结果中删除两次其值 (两次，因为我们在求和运算中已经把它加为正数了)
        return sum(nums) - (k - i) % 2 * min(nums) * 2



# @lc code=end


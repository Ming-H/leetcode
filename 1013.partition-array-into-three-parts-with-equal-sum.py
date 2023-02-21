#
# @lc app=leetcode id=1013 lang=python3
#
# [1013] Partition Array Into Three Parts With Equal Sum
#

# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%3!=0:
            return False 
        cnt, cumsum, target = 0, 0, total//3
        for item in nums:
            cumsum += item 
            if cumsum == target:
                cumsum = 0
                cnt += 1
        return cnt>=3


# @lc code=end


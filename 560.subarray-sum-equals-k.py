#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        sum[i]−sum[j]=k, the sum of elements lying between 
        indices i and j is k.
        """
        d = {}
        d[0] = 1
        Sum = 0
        count = 0
        for item in nums:
            Sum += item
            if Sum-k in d:
                count += d[Sum-k]
            d[Sum] = d.get(Sum, 0) + 1
        return count

        
# @lc code=end


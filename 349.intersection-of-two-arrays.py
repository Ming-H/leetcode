#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for item in nums1:
            if item not in res and item in nums2:
                res.append(item)
        return res  



# @lc code=end


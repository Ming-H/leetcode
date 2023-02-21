#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
from typing_extensions import dataclass_transform


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        res = []
        for item in nums1:
            d[item] = d.get(item, 0) + 1
        for item in nums2:
            if item in d and d[item]>0:
                res.append(item)
                d[item] -= 1
        return res 





# @lc code=end


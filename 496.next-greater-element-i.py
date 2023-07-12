#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        for item in nums2:
            while stack and item > stack[-1]:
                d[stack.pop()] = item
            stack.append(item)
        return [d.get(item, -1) for item in nums1]


# @lc code=end

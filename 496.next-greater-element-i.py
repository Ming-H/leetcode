#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, res  = [], []
        d = {}
        for item in nums2:
            while stack and item>stack[-1]:
                d[stack.pop()] = item 
            stack.append(item)
        for item in nums1:
            if item in d:
                res.append(d[item])
            else:
                res.append(-1)
        return res 



# @lc code=end


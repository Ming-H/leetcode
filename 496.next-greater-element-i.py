#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        for num in nums2:
            while stack != [] and num > stack[-1]:
                dic[stack.pop()] = num
            stack.append(num)

        res = []
        for num in nums1:
            if num in dic.keys():
                res.append(dic[num])
            else:
                res.append(-1)

        return res
# @lc code=end


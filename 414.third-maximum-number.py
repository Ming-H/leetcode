#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        v = [float('-inf'), float('-inf'), float('-inf')]
        for item in nums:
            if item not in v:
                if item>v[0]:
                    v = [item, v[0], v[1]]
                elif item>v[1]:
                    v = [v[0], item, v[1]]
                elif item>v[2]:
                    v = [v[0], v[1], item]
        return max(nums) if float('-inf') in v else v[2]




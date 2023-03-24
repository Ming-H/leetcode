#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # missing = len(nums)
        # for i, num in enumerate(nums):
        #     missing ^= i ^ num
        # return missing
        """
        遍历一遍，将 item 放到 item-1 的位置，最后0所处的位置
        加一即为所求
        """
        n = len(nums)
        return n * (n+1) // 2 - sum(nums)

        

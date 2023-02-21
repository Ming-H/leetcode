#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left <= right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            elif s<target:
                left += 1
            else:
                right -= 1
        return -1





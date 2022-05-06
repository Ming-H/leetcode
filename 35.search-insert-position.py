#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 二分查找
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] > target:
                high = mid -1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return low

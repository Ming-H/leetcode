#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r: # 注意 =
            mid =(l+r)//2
            if nums[mid] == target:
                return mid

            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1




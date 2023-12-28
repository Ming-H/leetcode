#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
class Solution:
    """
    https://www.cnblogs.com/grandyang/p/4539757.html

    把大于中枢点的数字放到左半边，把小于中枢点的放在右半边，

    这样中枢点是整个数组中第几大的数字就确定了，虽然左右两部
    分各自不一定是完全有序的，但是并不影响本题要求的结果，
    因为左半部分的所有值都大于右半部分的任意值，所以我们求出
    中枢点的位置，如果正好是 k-1，那么直接返回该位置上的数字；
    如果大于 k-1，说明要求的数字在左半部分，更新右边界，再求
    新的中枢点位置；反之则更新右半部分，求中枢点的位置
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums)-1
        while True:
            pos = self.partition(nums, left, right)
            if pos == k - 1:
                return nums[pos]
            if pos > k - 1:
                right = pos - 1
            else:
                left = pos + 1

    def partition(self, nums, left,  right):
        pivot = nums[left]
        l = left + 1
        r = right
        while l <= r:
            if nums[l] < pivot < nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            if nums[l] >= pivot:
                l += 1
            if nums[r] <= pivot:
                r -= 1
        nums[left], nums[r] = nums[r], nums[left]
        return r

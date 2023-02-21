#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        https://www.jianshu.com/p/a3cd9df6d9d1
        -将第1个数字加入解集；
        -依次读取后面的数字，如果此数字比解集中最后一个数字大，则将此数字追加到解集后，
         否则，用这个数字替换解集中第一个比此数字大的数，解集是有序的，因此查找可以用
         二分法，复杂度O(log n)；
        -最后的答案是解集的长度（而解集中保存的并不一定是合法解）。
        举个栗子，输入为[1,4,6,2,3,5]：
        -解集初始化为[1]；
        -读到4，将其追加到解集中，解集变为[1,4]；
        -读到6，将其追加到解集中，解集变为[1,4,6]；
        -读到2，用其替换解集中的4，解集变为[1,2,6]，注意此时解集不是一个合法解，因为2
         是在6后出现的，但是解集的长度始终标识着当前最长序列的长度；
        -读到3，用其替换解集中的6，解集变为[1,2,3]；
        -读到5，将其追加到解集中，解集变为[1,2,3,5]，得到答案为解集长度4。
        """
        if len(nums)==0:
            return 0
        res = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else:
                index = self.findIndex(res, nums[i])
                res[index] = nums[i]
        return len(res)


    def findIndex(self, nums, target):
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r = mid - 1
            else:
                l = mid + 1
        return l
        # if len(nums)==0:
        #     return 0
        # dp = [1 for _ in range(len(nums))]
        # for i in range(1,len(nums)):
        #     for j in range(i):
        #         if nums[i]>nums[j]:
        #             dp[i] = max(dp[i],dp[j]+1)
        # return max(dp)



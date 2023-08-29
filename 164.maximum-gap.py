#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
        bucket_size = (max_val-min_val)/(len(nums)-1)
        buckets = [[float('inf'), float('-inf')] for _ in range(len(nums)-1)]

        for item in nums:
            if item == max_val:
                continue
            index = int((item - min_val) / bucket_size)
            buckets[index][0] = min(buckets[index][0], item)
            buckets[index][1] = max(buckets[index][1], item)

        diff = 0
        pre_max = min_val
        for bucket in buckets:
            if bucket[0] == float('inf'):
                continue
            diff = max(diff, bucket[0]-pre_max)
            pre_max = bucket[1]
        diff = max(diff, max_val-pre_max)
        return diff

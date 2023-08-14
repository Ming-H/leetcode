#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        min_value = min(nums)
        max_value = max(nums)

        if min_value == max_value:
            return 0

        bucket_size = (max_value - min_value) / (len(nums) - 1)
        buckets = [[float('inf'), float('-inf')] for _ in range(len(nums) - 1)]

        for num in nums:
            if num == max_value:
                continue
            bucket_index = int((num - min_value) / bucket_size)
            bucket = buckets[bucket_index]
            bucket[0] = min(bucket[0], num)
            bucket[1] = max(bucket[1], num)

        max_diff = 0
        prev_max = min_value

        for bucket in buckets:
            if bucket[0] == float('inf'):
                continue
            max_diff = max(max_diff, bucket[0] - prev_max)
            prev_max = bucket[1]

        max_diff = max(max_diff, max_value - prev_max)

        return max_diff

#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2:
            return

        # solve 2-sum
        if N == 2:
            l, r = 0, len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append(result + [nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums)-N+1):   # careful about range
                if i > 0 and nums[i-1] == nums[i]:  # recursively reduce N
                    continue
                self.findNsum(nums[i+1:], target-nums[i],
                              N-1, result+[nums[i]], results)
        return

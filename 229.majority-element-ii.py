#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        count1, count2, item1, item2 = 0, 0, 0, 1
        for item in nums:
            if item == item1:
                count1 += 1
            elif item == item2:
                count2 += 1
            elif count1 == 0:
                item1, count1 = item, 1
            elif count2 == 0:
                item2, count2 = item, 1
            else:
                count1, count2 = count1-1, count2-1
        return [item for item in (item1, item2) if \
                        nums.count(item)>len(nums)//3]



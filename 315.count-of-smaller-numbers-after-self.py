#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of smaller Numbers After Self
#
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort(enum):
            mid = len(enum) // 2
            if mid:
                left, right = sort(enum[:mid]), sort(enum[mid:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        res[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        res = [0] * len(nums)
        sort(list(enumerate(nums)))
        return res

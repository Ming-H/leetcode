#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Time complexity : O(n)
        Space complexity : O(n)
        """
        """
        单次查询中：看来list 就是O(n)的；
        set做了去重,本质应该一颗红黑树（猜测，STL就是红黑树），复杂度O(logn)；
        dict类似对key进行了hash,然后再对hash生成一个红黑树进行查找，
        其查找复杂其实是O(logn),并不是所谓的O(1)。
        O(1)只是理想的实现，实际上很多hash的实现是进行了离散化的。
        dict比set多了一步hash的过程，so 它比set慢，不过差别不大。
        """
        res = 0
        nums = set(nums)
        for item in nums:
            if item-1 not in nums:
                cur = item
                cnt = 1
                while cur+1 in nums:
                    cur += 1
                    cnt += 1
                res = max(res, cnt)
        return res

    



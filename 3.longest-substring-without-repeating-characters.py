#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        顺序遍历，用字典保存未出现过的字符，若当前字符出现在字典，
        则start移动
        Time complexity : O(n)
        Space complexity (HashMap) : O(min(m, n))
        # [316] Remove Duplicate Letters
        """
        start = res = 0
        d = {}
        for i, item in enumerate(s):
            if item in d and start <= d[item]:
                start = d[item] + 1
            else:
                res = max(res, i-start+1)
            d[item] = i
        return res

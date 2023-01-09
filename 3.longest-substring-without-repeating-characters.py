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
        """
        start = maxlen = 0
        usedchar = {}
        for i, item in enumerate(s):
            if item in usedchar and start<=usedchar[item]:
                start = usedchar[item] + 1 #跳过前面出现过的字符
            else:
                maxlen = max(maxlen, i-start+1)
            usedchar[item] = i
        return maxlen
       


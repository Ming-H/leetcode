#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Time complexity : O(S)
        Space complexity : O(1)
        拿出第一个字符串，分别与后面所有的比较，求出最长公共头，求最小一个
        """
        if len(strs)==0:
            return ""
        str0=strs[0]
        Min=len(str0)
        for i in range(1,len(strs)):
            j=0
            while j<Min and j<len(strs[i]) and strs[i][j]==str0[j]:
                j+=1
            Min = min(Min, j)
        return str0[:Min]


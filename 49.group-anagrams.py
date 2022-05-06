#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Time Complexity: O(NK)
        Space Complexity: O(NK)
        """
        ans = dict()
        for item in strs:
            count = [0] * 26
            for c in item:
                count[ord(c)-ord('a')] += 1
            if tuple(count) not in ans:
                ans[tuple(count)] = [item]
            else:
                ans[tuple(count)].append(item)
        return ans.values()




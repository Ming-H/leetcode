#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        The time complexity of this solution is O(n), 
        where n is the length of s. 
        """
        pCount = [0] * 26
        sCount = [0] * 26
        result = []
        for char in p:
            pCount[ord(char) - ord('a')] += 1
        left = 0
        for right in range(len(s)):
            sCount[ord(s[right]) - ord('a')] += 1
            if right - left + 1 > len(p):
                sCount[ord(s[left]) - ord('a')] -= 1
                left += 1
            if pCount == sCount:
                result.append(left)
        return result



        
# @lc code=end


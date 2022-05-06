#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1==s2 or s1==s2[::-1]:
            return True

        for i in range(1, len(s1)):
            if sorted(s1[:i])==sorted(s2[:i]):
                if self.isScramble(s1[i:],s2[i:]) and self.isScramble(s1[:i],s2[:i]):
                    return True
            elif sorted(s1[:i])==sorted(s2[-i:]):
                if self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i]):
                    return True
        return False 



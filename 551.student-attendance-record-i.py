#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        for i in range(len(s)): 
            if s[i] == 'A': 
                if a>=1: 
                    return False
                a += 1
            elif s[i] == 'L' and 0 < i < len(s)-1 \
                            and s[i-1] == 'L' == s[i+1]: 
                return False
        return True
# @lc code=end


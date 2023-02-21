#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False 
        d = {}
        for item in magazine:
            d[item] = d.get(item, 0) + 1
        for item in ransomNote:
            if item not in d:
                return False 
            else:
                if d[item] == 0:
                    return False 
                else:
                    d[item] -= 1
        return True 



        
# @lc code=end


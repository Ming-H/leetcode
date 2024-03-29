#
# @lc app=leetcode id=599 lang=python3
#
# [599] Minimum Index Sum of Two Lists
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {x: list1.index(x) + list2.index(x) 
                for x in set(list1) & set(list2)}
        return [x for x in d if d[x] == min(d.values())]
        
# @lc code=end


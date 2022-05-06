#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        i = 0
        count = 0
        while i<len(flowerbed):
            if flowerbed[i]==0 and (flowerbed[i-1]==0 or i==0)\
                     and (flowerbed[i+1]==0 or i==len(flowerbed)-1):
                flowerbed[i] = 1
                count += 1
            i += 1
        return count>=n

# @lc code=end


#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        Time complexity : O(n)
        Space complexity : O(1)
        """
        smallestTwo = [float('inf')]*2
        largestThree = [float('-inf')]*3
        for item in nums:
            if item <= smallestTwo[0]:
                smallestTwo[0] = item
                smallestTwo.sort(reverse=True)
            if item >= largestThree[0]:
                largestThree[0] = item
                largestThree.sort()
        return max(smallestTwo[0]*smallestTwo[1]*largestThree[2], 
                   largestThree[0]*largestThree[1]*largestThree[2])




# @lc code=end


#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if not height or len(height) < 3:
            return 0
        volume = 0
        left, right = 0, len(height) - 1
        l_max, r_max = height[left], height[right]
        while left <= right:
            if height[left] < height[right]:
                if height[left] > l_max:
                    l_max = height[left]
                else:
                    volume += l_max - height[left]
                left += 1
            else:
                if height[right] > r_max:
                    r_max = height[right]
                else:
                    volume += r_max - height[right]
                right -= 1
        return volume
        


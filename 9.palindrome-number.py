#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x_copy = x
        tmp = 0
        while x>0:
            tmp *= 10
            tmp += x %10
            x = x//10
        if tmp == x_copy:
            return True
        else:
            return False


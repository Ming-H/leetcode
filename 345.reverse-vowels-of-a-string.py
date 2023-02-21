#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s 
        l = list(s)
        i = 0
        j = len(l)-1
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        while i<j:
            if l[i] in vowels and l[j] in vowels:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
            if l[i] not in vowels:
                i += 1
            if l[j] not in vowels:
                j -= 1
        return "".join(l)

        


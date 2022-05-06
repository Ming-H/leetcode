#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)
        if (len(l)==0):
            return s
        i = 0
        j = len(l)-1
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        while True:
            while (l[i] not in vowels):
                i += 1
                if i > len(l)-1:
                    break
            while (l[j] not in vowels):
                j -= 1
                if j < 0:
                    break
            if i >= j:
                break
            l[i], l[j] = l[j], l[i]
            
            i += 1
            j -= 1
        return "".join(l)

        


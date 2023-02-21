#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0 
        N = len(s)
        for a in range(N):
            
            ##Count odd palindromic substrings like a, aaa
            i,j = a, a
            while 0<=i<N and 0<=j<N and s[i] == s[j]:
                result += 1
                i -= 1
                j += 1
                
            ##Count even palindromic substrings like aa, aaaa
            i,j = a, a+1
            while 0<=i<N and 0<=j<N and s[i] == s[j]:
                result += 1
                i -= 1
                j += 1
                
        return result



# @lc code=end


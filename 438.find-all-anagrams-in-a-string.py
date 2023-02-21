#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict=collections.Counter(p)
        s_dict=collections.Counter(s[:len(p)])
        res=[]
        i=0
        j=len(p)
        while j<=len(s):
            if s_dict==p_dict:
                res.append(i)
            s_dict[s[i]]-=1
            if s_dict[s[i]]<=0:
                s_dict.pop(s[i])
            if j<len(s):    
                s_dict[s[j]]+=1
            j+=1
            i+=1
        return res  



        
# @lc code=end


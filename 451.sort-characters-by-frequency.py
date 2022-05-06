#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        res=""
        for ch in s:
            d[ch]=d.get(ch,0)+1
        
        a=sorted(d.items(), key=lambda x: x[1], reverse=True)
        for i in range(len(a)):
            res+=a[i][0]*a[i][1]
        return res

# @lc code=end


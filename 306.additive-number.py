#
# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#

# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def add(prev,curr,index):
            if index==len(num):
                return True
            total=str(int(prev)+int(curr))
            if total==num[index:index+len(total)]:
                return add(curr,total,index+len(total))
            else:
                return False
        
        for i in range(len(num)):
            if num[0]=='0' and i>0:
                break
            for j in range(i+1, len(num)):
                prev=num[0:i+1]
                curr=num[i+1:j+1]
                if curr[0]=='0' and len(curr)>1:
                    break
                total=str(int(prev)+int(curr))
                if total==num[j+1:j+1+len(total)]:
                    if  add(curr,total,j+1+len(total)):
                        return True

        return False
        
# @lc code=end


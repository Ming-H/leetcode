#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            ss =  0-int(''.join([item for item in str(x)[1:]][::-1]))
            if ss<-2**(31):
                return 0
            else:
                return ss
        else:
            ss =  int(''.join([item for item in str(x)][::-1]))
            if ss>2**(31):
                return 0
            else:
                return ss



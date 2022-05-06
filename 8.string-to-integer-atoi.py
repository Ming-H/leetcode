#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
class Solution:
    def myAtoi(self, str):
        str = str.strip()
        flag = 1
        result=0
        i=0
        number = '0123456789'
        if not str or len(str) == 0:
            return 0
        if str [0]=='-':
            flag =-1
            i=i+1
        elif str[0]=='+':
            i=i+1
        while(i<len(str)):
            if str[i] in number:
                result = result *10 +int(str[i])
            else:
                break
            i=i+1
        if flag*result >  2147483647:
            return   2147483647
        if flag*result <  -2147483648:
            return -2147483648
        return flag*result

        


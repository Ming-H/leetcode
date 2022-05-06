#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Time complexity : O(n^2)
        Space complexity : O(1)
        """
        # maxl = 0
        # start = 0
        # for i in range(len(s)):
        #     if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
        #         start = i - maxl - 1
        #         maxl += 2
                
        #     if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
        #         start = i - maxl
        #         maxl += 1
        # return s[start: start + maxl]   
        
        """
        Approach 4: Expand Around Center
        In fact, we could solve it in O(n^2) time using only constant space.
        We observe that a palindrome mirrors around its center. Therefore, 
        a palindrome can be expanded from its center, and there are 
        only 2n−1 such centers. You might be asking why there are 2n−1 
        but not n centers? The reason is the center of a palindrome 
        can be in between two letters. Such palindromes have even number 
        of letters (such as "abba") and its center are between the two 'b's.
        """
        if  len(s)<1:
            return ""
        
        def expand(s, L, R):
            while L>=0 and R<len(s) and s[L]==s[R]:
                L -= 1
                R += 1
            return R-L-1

        start, end = 0, 0
        for i in range(len(s)):
            len1 = expand(s, i, i)
            len2 = expand(s, i, i+1)
            len_max = max(len1, len2)
            if len_max > end-start:
                start = i - (len_max-1)//2
                end = i + len_max//2
        return s[start: end+1]


        
        """
        step1:给每个字符左右都加上特殊字符比如'#'，处理后，能使字符串s长度为奇
        step2：现在的问题变成如何高效求得RL数组
        定义： RL：是一个回文半径数组
              RL[i]：以第i个字符为对称轴的回文半径
              maxRight：当前访问到的所有回文串中最右边的字符位置
              Pos：maxRight对应回文串的对称轴所在位置
              i：第i个字符
              j: i关于pos的对称点

        （1）：i在maxright右边：就是说以i为对称轴的回文串还没被访问。
                        这时，以i为中心向两边扩展，当达到边界or字符不相等时停止。
        （2）：i在maxright左边：扫到了一部分以i为对称轴的子串。
                       这时，令以i为对称轴的回文半径RL【i】= min(RL[j],maxright-i)
                        然后再以i为中心向两边扩展，直到左！=右且到达边界
                        最后更新maxright=max(maxright,RL[i]+i-1)且若maxright变，
                        Pos会变为Pos=i
        
        原文链接：https://blog.csdn.net/zuanfengxiao/article/details/80341483
        https://blog.csdn.net/haut_ykc/article/details/52137496
        """
        # s='#'+'#'.join(s)+'#'#step1
    
        # RL=[0]*len(s) #各种初始化一下，RL是回文半径数组
        # MaxRight=0
        # Pos=0
        # Maxlen=0
    
        # for i in range(len(s)):
        #     if i<MaxRight: # i在maxright左边
        #         RL[i]=min(RL[2*Pos-i], MaxRight-i)
        #     else:  # i在maxright右边，以i为中心的回文串还没扫到，此时，以i为中心向两边扩展
        #         RL[i]=1 # RL=1：只有自己
    
        #     #以i为中心扩展，直到左！=右or达到边界(先判断边界)
        #     while i-RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]]==s[i+RL[i]]:
        #         RL[i]+=1
    
        #     #更新Maxright pos:
        #     if RL[i]+i-1>MaxRight:
        #         MaxRight=RL[i]+i-1
        #         Pos=i
    
        #     #更新最长回文子串的长;
        #     Maxlen=max(Maxlen, RL[i])
        # s=s[RL.index(Maxlen)-(Maxlen-1): RL.index(Maxlen)+(Maxlen-1)]
        # s=s.replace('#','')
        # return s


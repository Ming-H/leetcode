#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cnt = 0
        nchar = 0
        temp = []
        for i, w in enumerate(words):            
            if nchar+len(w)+cnt <= maxWidth: #if the length add current word  is less than the max, add the word
                temp.append(w)
                cnt += 1
                nchar += len(w)
           
            else:            
                if cnt == 1: #if there is only one word, aligh left
                    temp_char = temp[0]+" "*(maxWidth-len(temp[0]))
                
                else: #if more than two words
                    space = (maxWidth - nchar) // (cnt-1) #count how many space needed to adjust evenly
                    mod = (maxWidth - nchar) % (cnt-1)  #count how many offse to add
                    temp_char = ""
                    for t in temp[:-1]:
                        temp_char += t
                        temp_char += " "*space
                        if mod > 0:
                            temp_char += " " #if the offset is > 0 add the offset space
                            mod -= 1
                    temp_char += temp[-1] #add the last word to the end
                res.append(temp_char)
                cnt = 1 #rememer to add the current word at the end of the for loop
                nchar = len(w)
                temp = [w]
            if i == len(words)-1: #if the current word is the last word, add anyways
                temp_char = ' '.join(temp) #join by space and add remaining extra space
                if len(temp_char) < maxWidth:
                    temp_char += " "*(maxWidth-len(temp_char))
                res.append(temp_char)
        return res





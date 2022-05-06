#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        O(n) Time. 
        O(n) Space.
        """
        if k < 0:
            return 0
        from collections import Counter
        count = Counter(nums)
        pairs = set([])
        
        for num in count.keys():
			#Special case: If k == 0, then there needs to be at least two occurences of a particular num in nums 
			#in order for there to be a pair (num, num).
            if k == 0:
                if count[num] > 1:
                    pairs.add((num, num))
					
			#Regular case: k != 0. Simply check if num + k is a member of the array nums.
			#Insert the pair into the set of pairs (smallerNum, largerNum) so that there are no duplicate pairs.
            else:
                otherNum = num + k
                if otherNum in count:
                    pairs.add((num, otherNum) if num <= otherNum \
                                            else (otherNum, num))
                    
        return len(pairs)
        
# @lc code=end


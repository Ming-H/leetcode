#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
class Solution:
    def threeSumClosest(self, num: List[int], target: int) -> int:
        """
        no duplicate
        """
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum
                #更新res
                if abs(sum - target) < abs(result - target):
                    result = sum
                
                if sum < target:
                    j += 1
                    
                elif sum > target:
                    k -= 1
            
        return result


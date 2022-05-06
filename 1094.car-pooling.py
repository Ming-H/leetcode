#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        统计出每个站上的人数和下的人数
        然后遍历所有的站看每个站过后车上还剩多少人
        """
        stops = [0] * 1001
        for item in trips:
            #上车
            stops[item[1]] += item[0]
            #下车
            stops[item[2]] -= item[0]
        sumer = 0
        for p in stops:
            sumer += p
            if sumer > capacity:
                return False
        return True

# @lc code=end


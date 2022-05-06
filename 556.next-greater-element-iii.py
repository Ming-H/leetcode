#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        https://blog.csdn.net/fuxuemingzhu/article/details/82113731
        """
        nums = list(str(n))
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        if i == 0:
            return -1
        self.reverse(nums, i, n - 1)
        for j in range(i, n):
            if nums[j] > nums[i-1]:
                nums[i-1], nums[j] = nums[j], nums[i-1]
                break
        ans = int("".join(nums))
        if ans > 1 << 31: #所以带符号32位int类型整数为-2147483648~2147483647
            return -1
        else:
            return ans

    def reverse(self, nums, i, j):
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i +=1 
            j -= 1

# @lc code=end


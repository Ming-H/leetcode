#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        return self.mergesort_and_count(nums, 0, len(nums)-1)

    def merge(self, A, start, mid, end):
        L = []
        R = []
        n1 = mid - start + 1
        n2 = end - mid
        for i in range(0, n1):
            L.append(A[start+i])
        for j in range(0, n2):
            R.append(A[mid+1+j]) 
        i = 0
        j = 0
        for k in range(start, end+1):
            if j >= n2 or (i < n1 and L[i] <= R[j]):
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1

    def mergesort_and_count(self, A, start, end):
        if (start < end):
            mid = int((start + end) / 2)
            count = self.mergesort_and_count(A, start, mid) + self.mergesort_and_count(A, mid + 1, end)
            j = mid + 1
            
            for i in range(start, mid+1):
                while j<=end and A[i]>A[j]*2:
                    j += 1
                count += j-(mid+1)
            self.merge(A, start, mid, end)
            return count
        else:
            return 0


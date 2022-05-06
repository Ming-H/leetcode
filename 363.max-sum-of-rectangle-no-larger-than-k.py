#
# @lc app=leetcode id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#

# @lc code=start
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ret=float('-inf')
        def mergeSort(arr):
            nonlocal ret
            n=len(arr)
            if n<=1:
                return arr
            mid=n//2
            arr1=mergeSort(arr[:mid])
            arr2=mergeSort(arr[mid:])            
            res=[]
            i,j,p=0,0,0
            n1,n2=len(arr1),len(arr2)
            while i<n1 or j<n2:
                v1=arr1[i] if i<n1 else float('inf')
                v2=arr2[j] if j<n2 else float('inf')
                if v1<=v2:
                    res.append(v1)
                    i+=1
                else:
                    while p<n1 and v2-arr1[p]>k:
                        p+=1
                    if p<n1 and v2-arr1[p]>ret:
                        ret=v2-arr1[p]
                    res.append(v2)
                    j+=1
            return res
        n=len(matrix)
        m=len(matrix[0]) if n else 0
        if n>m:
            return self.maxSumSubmatrix([list(a) for a in zip(*matrix)],k)
        colPrefix=[[0] for _ in range(m)]
        for i in range(n):
            for j in range(m):
                colPrefix[j].append(colPrefix[j][-1]+matrix[i][j])        
        arr=[0]*(m+1)
        for i in range(n):
            for i2 in range(i,n):
                low=0
                tmpMax=float('-inf')
                for j in range(1,m+1):
                    arr[j]=arr[j-1]+colPrefix[j-1][i2+1]-colPrefix[j-1][i]
                    low=min(low,arr[j])
                    tmpMax=max(tmpMax,arr[j]-low)
                if tmpMax<=k:
                    ret=max(ret,tmpMax)
                else:
                    mergeSort(arr)
                if ret==k:
                    return k
        return ret
# @lc code=end


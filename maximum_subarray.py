class Solution:
    """
    @see https://oj.leetcode.com/problems/maximum-subarray/
    """
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        idx = [i for i,n in enumerate(A) if n > 0]
        l = len(idx)
        if l == 0:
            return max(A)
        #d is the max value of each array which begin of each positive value
        d = {idx[l-1]: A[idx[l-1]]} 
        m = A[idx[l-1]]
        for i in range(1, l):
            s = sum(A[idx[l-i-1]:idx[l-i]])
            if s+d[idx[l-i]] > A[idx[l-i-1]]:
                d[idx[l-i-1]] = s + d[idx[l-i]]
            else:
                d[idx[l-i-1]] = A[idx[l-i-1]]
            if m < d[idx[l-i-1]]:
                m = d[idx[l-i-1]]
        return m

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([1,2,-1,-2,2,1,-2,1,4,-5,4]))



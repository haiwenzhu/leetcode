class Solution:
    """
    @see https://oj.leetcode.com/problems/spiral-matrix-ii/
    """
    # @return a list of lists of integer
    def generateMatrix(self, n):
        res = []
        for i in range(n):
            res.append([])
        nums = [i+1 for i in range(n*n)]
        idx = 0
        for i in range((n+1) // 2):
            res[i][i:i] = nums[idx:idx+n-2*i]
            idx += n-2*i
            for j in range(i+1, n-i-1):
                res[j][i:i] = nums[idx:idx+1]
                idx += 1
            if n-i-1 > i:
                res[n-i-1][i:i] = reversed(nums[idx:idx+n-2*i])
                idx += n-2*i
            if i < n-i-1:
                for j in range(i+1, n-i-1):
                    res[n-j-1][i:i] = nums[idx:idx+1]
                    idx += 1
        return res
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.generateMatrix(3))

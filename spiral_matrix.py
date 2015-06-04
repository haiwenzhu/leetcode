class Solution:
    """
    @see https://oj.leetcode.com/problems/spiral-matrix/
    """
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):    
        m = len(matrix)
        n = 0 if m==0 else len(matrix[0])
        l = 0
        res = []
        for i in range(min(m+1,n+1) // 2):
            res.extend(matrix[i][i:n-i])
            for j in range(i+1, m-i):
                res.append(matrix[j][n-i-1])
            if m-i-1 > i:
                res.extend(reversed(matrix[m-i-1][i:n-i-1]))
            if i < n-i-1:
                for j in range(i+1, m-i-1):
                    res.append(matrix[m-j-1][i])
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.spiralOrder([[1],[2],[3]]))

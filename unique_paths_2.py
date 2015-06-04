class Solution:
    """
    @see https://oj.leetcode.com/problems/unique-paths-ii/
    """
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = 0 if m == 0 else len(obstacleGrid[0])
        d = {}
        for i in range(m):
            d[i] = {}
            for j in range(n):
                d[i][j] = -1
        self.d = d
        return self._uniquePaths(0, 0, m, n, obstacleGrid) 

    def _uniquePaths(self, i, j, m, n, obstacleGrid):
        if self.d[i][j] >= 0:
            return self.d[i][j]
        if obstacleGrid[i][j] == 1:
            p = 0
        elif i == m-1 and j == n-1:
            p = 1
        elif i == m-1:
            p = self._uniquePaths(i, j+1, m, n, obstacleGrid)
        elif j == n-1:
            p = self._uniquePaths(i+1, j, m, n, obstacleGrid)
        else:
            p = self._uniquePaths(i, j+1, m, n, obstacleGrid) + self._uniquePaths(i+1, j, m, n, obstacleGrid)
        self.d[i][j] = p
        return p

if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePathsWithObstacles([[0,0,0],[1,1,1],[0,0,0]]))

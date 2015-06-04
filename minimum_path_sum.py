class Solution:
    """
    @see https://oj.leetcode.com/problems/minimum-path-sum/
    """
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        self.grid = grid
        self.m =  len(grid)
        self.n = 0 if self.m == 0 else len(grid[0])
        d = {}
        for i in range(self.m):
            d[i] = {}
            for j in range(self.n):
                d[i][j] = -1
        self.d = d
        return self._min(0, 0)

    def _min(self, i, j):
        if self.d[i][j] >= 0:
            return self.d[i][j]
        if i == self.m-1 and j == self.n-1:
            res = self.grid[i][j]
        elif i == self.m-1:
            res = self.grid[i][j] + self._min(i, j+1)
        elif j == self.n-1:
            res = self.grid[i][j] + self._min(i+1, j)
        else:
            res = self.grid[i][j] + min(self._min(i+1, j), self._min(i, j+1))
        self.d[i][j] = res
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.minPathSum([[1,1,1],[2,2,2],[3,3,3]]))

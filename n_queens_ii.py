class Solution:
    """
    @see https://leetcode.com/problems/n-queens-ii/
    """
    # @return a list of lists of string
    def totalNQueens(self, n):
        self.n = n
        self.n2 = (self.n+1)//2
        self.n3 = self.n // 2
        self.nrg = range(n)
        self.res = 0
        cb = []
        for i in self.nrg:
            cb.append([])
            for j in self.nrg:
                cb[i].append('*')
        for i in range(0, self.n):
            cb1 = [r[0:] for r in cb]
            self._solve(cb1, 0, i)
        return self.res

    def _solve(self, cb, i, j):
        cb[i][j] = 'Q'
        if i == self.n - 1:
            self.res += 1
        else:
            for k in range(i+1, self.n):
                cb[k][j] = '.'
                if j+i-k >= 0:
                    cb[k][j+i-k] = '.'
                if j+k-i < self.n:
                    cb[k][j+k-i] = '.'
            for k in self.nrg:
                if cb[i][k] == '*':
                    cb[i][k] = '.'
            if cb[i+1].count('*') > 0:
                for k in self.nrg:
                    if cb[i+1][k] == '*':
                        cb1 = [r[0:] for r in cb]
                        self._solve(cb1, i+1, k)

if __name__ == "__main__":
    solution = Solution()
    output = solution.solveNQueens(7)
    print(output)

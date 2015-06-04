class Solution:
    """
    @see https://oj.leetcode.com/problems/set-matrix-zeroes/
    """
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        row1 = 1
        col1 = 1
        m = len(matrix)
        n = 0 if m == 0 else len(matrix[0])
        if m > 0:
            if matrix[0].count(0) > 0:
                row1 = 0
            for i in range(m):
                if matrix[i][0] == 0:
                    col1 = 0
                    break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        if row1 == 0:
            for j in range(n):
                matrix[0][j] = 0
        if col1 == 0:
            for i in range(m):
                matrix[i][0] = 0
        return matrix

    #A solution use m+n space
    def _solution(self, matrix):
        rows = []
        cols = []
        m = len(matrix)
        n = 0 if m == 0 else len(matrix[0])

        for i in range(m):
            c = matrix[i].count(0)
            if c > 0:
                rows.append(i)
                j = 0
                while c > 0:
                    j = matrix[i].index(0, j)
                    if j not in cols:
                        cols.append(j)
                    j += 1
                    c -= 1
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0
        return matrix

if __name__ == "__main__":
    solution = Solution()
    print(solution.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]))
                    

class Solution:
    """
    @see https://oj.leetcode.com/problems/rotate-image/
    """
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(0, (n+1)//2):
            for j in range(i, n-i-1):
                tmp = matrix[i][j]
                tmpi, tmpj = i, j
                #while n=3 and i=0,j=0
                #this loop will set (0,0)->(2,0)->(2,2)->(0,2)
                while True:
                    i1 = n - tmpj - 1
                    j1 = tmpi
                    if i == i1 and j == j1:
                        matrix[tmpi][tmpj] = tmp
                        break
                    matrix[tmpi][tmpj] = matrix[i1][j1]
                    tmpi = i1
                    tmpj = j1
        return matrix

if __name__ == "__main__":
    solution = Solution()
    print(solution.rotate([[1,2,3],[1,2,3],[1,2,3]]))


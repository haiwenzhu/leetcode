class Solution:
    """
    @see https://oj.leetcode.com/problems/valid-sudoku/
    """
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(0, 9):
            if not self._isValid(board[i]):
                return False
            col = []
            for j in range(0, 9):
                col.append(board[j][i])
                if i%3 == 0 and j%3==0:
                    item = []
                    for m in range(i, i+3):
                        for n in range(j, j+3):
                            item.append(board[m][n])
                            if not self._isValid(item):
                                return False
            if not self._isValid(col):
                return False

        return True

    def _isValid(self, vals):
        for v in vals:
            if v != '.' and vals.count(v) > 1:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    board = []
    for i in range(0, 9):
        board.append([1,2,3,4,5,6,7,8,9])
    board = ["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
    print(solution.isValidSudoku(board))

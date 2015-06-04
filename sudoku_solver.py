class Solution:
    """
    @see https://leetcode.com/problems/sudoku-solver/
    """
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.idx = range(0, 9)
        self.num = [str(i) for i in range(1, 10)]
        self.board = board
        self.candidates = []
        self.blank = []
        self.solved = True
        for r in self.idx:
            self.candidates.append([])
            self.board[r] = list(self.board[r])
            for c in self.idx:
                if self.board[r][c] == '.':
                    self.candidates[r].append(self.getCandidates(r, c))
                    self.blank.append((r,c))
                else:
                    self.candidates[r].append('')
        rc = (0,0)
        while len(self.blank) > 0:
            flag = False
            candidates = 9
            rc = (0, 0)
            for r,c in self.blank:
                l = len(self.candidates[r][c])
                if l == 1:
                    self.board[r][c] = self.candidates[r][c][0]
                    self.candidates[r][c] = ''
                    self.blank.pop(self.blank.index((r,c)))
                    self.refreshCandidates(r, c)
                    flag = True
                    break
                else:
                    if candidates > l:
                        candidates = l
                        rc = (r, c)
            if not flag:
                self.solved = False
                break
        if not self.solved:
            r = rc[0]
            c = rc[1]
            for v in self.candidates[r][c]:
                tmpboard = self._copyBoard()
                tmpboard[r][c] = v
                solver = Solution()
                solver.solveSudoku(tmpboard)
                if solver.solved:
                    self.solved = True
                    for r in self.idx:
                        for c in self.idx:
                            self.board[r][c] = solver.board[r][c]
                    return
            
    def _copyBoard(self):
        board = []
        for row in self.board:
            board.append(row[0:])
        return board

    def refreshCandidates(self, r, c):
        val = self.board[r][c]
        for i in self.idx:
            if self.board[r][i] == '.':
                self.candidates[r][i] = self.getCandidates(r, i)
            if self.board[i][c] == '.':
                self.candidates[i][c] =  self.getCandidates(i, c)
        for i,j in self.getBoardIdx(r, c):
            if self.board[i][j] == '.':
                self.candidates[i][j] = self.getCandidates(i, j)
        

    def getCandidates(self, r, c):
        nums = self.getRow(r, c)
        nums.extend(self.getColumn(r, c))
        nums.extend(self.getBoard(r, c))
        return [i for i in self.num if i not in nums]

    def getRow(self, r, c):
        return self.board[r][0:]
        #return [self.board[r][i] for i in self.idx] 

    def getColumn(self, r, c):
        return [self.board[i][c] for i in self.idx]

    def getBoard(self, r, c):
        r = (r//3) * 3
        c = (c//3) * 3
        return [self.board[i][j] for i in range(r, r+3) for j in range(c, c+3)]

    def getBoardIdx(self, r, c):
        r = (r//3) * 3
        c = (c//3) * 3
        return [(i, j) for i in range(r, r+3) for j in range(c, c+3)]

if __name__ == "__main__":
    solution = Solution()
    board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
    solution.solveSudoku(board)
    print(board)
        

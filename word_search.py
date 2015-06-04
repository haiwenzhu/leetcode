class Solution:
    """
    @see https://oj.leetcode.com/problems/word-search/
    """
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        m = len(board)
        n = 0 if m == 0 else len(board[0])
        d = {}
        for c in word:
            d[c] = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in d:
                    d[board[i][j]].append((i,j))
        l = len(word)
        if l >= 1:
            for p in d[word[0]]:
                if self._search(word[1:], d, [p], m, n):
                    return True
        return False

    def _search(self, target, d, path, m, n):
        if len(path) == 0:
            return False
        elif len(target) == 0:
            return True
        else:
            p = path[-1]
            next = []
            if p[0] > 0:
                next.append((p[0]-1, p[1]))
            if p[0] < m-1:
                next.append((p[0]+1, p[1]))
            if p[1] > 0:
                next.append((p[0], p[1]-1))
            if p[1] < n-1:
                next.append((p[0], p[1]+1))
            for p1 in next:
                if p1 not in path and p1 in d[target[0]]:
                    new_path = path[0:]
                    new_path.append(p1)
                    if self._search(target[1:], d, new_path, m, n):
                        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.exist(["a"], "a"))

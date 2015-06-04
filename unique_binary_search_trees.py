class Solution:
    """
    @see https://oj.leetcode.com/problems/unique-binary-search-trees/
    """
    # @return an integer
    def numTrees(self, n):
        res = 0
        for num in range(1, n+1):
            res += self._num(num, 1, n)
        return res

    def _num(self, root, minval, maxval):
        if root-minval <= 1 and maxval-root <= 1:
            res = 1
        else:
            if root - minval > 1:
                res1 = 0
                for val in range(minval, root):
                    res1 += self._num(val, minval, root-1)
            else:
                res1 = 1
            if maxval - root > 1:
                res2 = 0
                for val in range(root+1, maxval+1):
                    res2 += self._num(val, root+1, maxval)
            else:
                res2 = 1
            res = res1 * res2
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.numTrees(2))

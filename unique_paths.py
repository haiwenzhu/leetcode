class Solution:
    """
    @see https://oj.leetcode.com/problems/unique-paths/
    meet this problem in baixin's interview
    """
    # @return an integer
    def uniquePaths(self, m, n):
        #if m == 1 or n == 1:
        #    return 1
        #else:
        #    return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

        # result is C(m+n-2, n-1)
        res = 1
        res1 = 1
        for i in range(1, m):
            res *= (m+n-i-1)
            res1 *= i
        return res/res1


if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePaths(3,7))

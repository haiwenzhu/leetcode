class Solution:
    dt = {0:0,1:1,2:2}
    """
    @see https://oj.leetcode.com/problems/climbing-stairs/
    """
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n in self.dt:
            return self.dt[n]
        else:
            self.dt[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.dt[n]

if __name__ == "__main__":
    solution =  Solution()
    print(solution.climbStairs(4))
    print(solution.climbStairs(5))

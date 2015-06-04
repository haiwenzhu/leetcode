class Solution:
    """
    @see https://oj.leetcode.com/problems/powx-n/
    """
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1/x
        else:
            if n > 0:
                if n % 2 == 0:
                    return pow(x*x, n//2)
                else:
                    return pow(x*x, n//2) * x 
            else:
                return pow(pow(x, -n), -1)
       
if __name__ == "__main__":
    solution = Solution()
    print(solution.pow(0.00001, 2147483647))

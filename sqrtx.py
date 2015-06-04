class Solution:
    """
    @see https://leetcode.com/problems/sqrtx/
    """
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        i = 0
        j = x
        while i <= j:
            m = (i+j) // 2
            mm = m * m
            if mm == x:
                break
            elif mm > x:
                j = m - 1
            else:
                if (m+1) * (m+1) > x:
                    break
                i = m + 1
        return m

if __name__ == "__main__":
    solution = Solution()
    print(solution.mySqrt(4))
    print(solution.mySqrt(144))
    print(solution.mySqrt(2))

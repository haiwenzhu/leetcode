class Solution:
    """
    @see https://oj.leetcode.com/problems/jump-game/
    """
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        n = len(A)
        j = -1
        target = n-1
        for i in range(n-1):
            if A[n-i-2] + n-i-2 >= target:
                target = n-i-2
        return target <= 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.canJump([2,3,1,1,4]))
    print(solution.canJump([2,0]))

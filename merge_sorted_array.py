class Solution:
    """
    @see https://oj.leetcode.com/problems/merge-sorted-array/
    """
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        idx = 0
        for v in B:
            while idx < m and v > A[idx]:
                idx += 1
            A[idx:idx] = [v]
            m += 1
        return A

if __name__ == "__main__":
    solution = Solution()
    print(solution.merge([1,3],2,[2,4],2))
    print(solution.merge([],0,[],0))



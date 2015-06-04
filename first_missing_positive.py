class Solution:
    """
    @see https://leetcode.com/problems/first-missing-positive/
    """
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        i = 0
        while i < n:
            if A[i] <= 0 or A[i] > n or A[i] == i+1:
                i += 1
            else:
                tmp = A[A[i]-1]
                if tmp == A[i]:
                    #if the value of A[i]-1 is A[i], no need to swap
                    A[i] = 0
                else:
                    A[A[i]-1] = A[i]
                    A[i] = tmp
        i = 0
        while i < n:
            if A[i] != i+1:
                return i+1
            i += 1
        return n+1

if __name__ == "__main__":
    solution = Solution()
    print(solution.firstMissingPositive([3,4,2,1]))

class Solution:
    """
    @see https://leetcode.com/problems/trapping-rain-water/
    """
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        i = 0
        j = len(A) - 1
        sum = 0
        while i < j and A[i] == 0:
            i += 1
        while i < j and A[j] == 0:
            j -= 1
        while i < j:
            if A[i] <= A[j]:
                k = i + 1
                while k <= j and A[k] < A[i]:
                    sum += A[i] - A[k]
                    k += 1
                i = k
            else:
                k = j - 1
                while k >= i and A[k] < A[j]:
                    sum += A[j] - A[k]
                    k -= 1
                j = k
        return sum

if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

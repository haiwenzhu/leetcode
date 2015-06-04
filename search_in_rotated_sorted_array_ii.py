class Solution:
    """
    @see https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
    """
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        n = len(A)
        if n == 0:
            return -1
        while n > 1 and A[0] == A[-1]:
            A.pop(0)
            n -= 1
        a1 = A[0]
        an = A[-1]
        i = 0
        j = n-1
        while i <= j:
            mid = (i+j) // 2
            if target == A[mid]:
                return True
            if A[mid] <= an:
                if target < A[mid] or target > an:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if target > A[mid] or target < a1:
                    i = mid + 1
                else:
                    j = mid - 1
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.search([1,1,3,1], 3))

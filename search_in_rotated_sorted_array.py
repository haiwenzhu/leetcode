class Solution:
    """
    @see https://leetcode.com/problems/search-in-rotated-sorted-array/
    """
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        n = len(A)
        if n == 0:
            return -1
        i = 0
        j = n-1
        while True:
            mid = (i+j) // 2
            if A[mid] < A[n-1]:
                j = mid -1
            elif mid+1 < n and A[mid] < A[mid+1]:
                i = mid + 1
            else:
                break
        if target > A[mid]:
            return -1
        elif target <= A[n-1]:
            i = mid + 1 if mid != n-1 else n-1
            j = n - 1
        else:
            i = 0
            j = mid
        # binary search
        while i <= j:
            mid = (i+j) // 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.search([], 1))

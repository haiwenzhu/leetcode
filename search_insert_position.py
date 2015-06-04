class Solution:
    """
    @see https://oj.leetcode.com/problems/search-insert-position/
    """
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        n = len(A)
        min = 0
        max = n - 1
        mid = -1
        while min <= max:
            mid = (min+max) // 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                max = mid - 1
                if max < 0:
                    return 0
                elif A[max] < target:
                    return mid
            else:
                min = mid + 1
                if min >= n:
                    return n
                elif A[min] > target:
                    return mid+1
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInsert([1,2,5,6], 5))
    print(solution.searchInsert([1,2,5,6], 0))
    print(solution.searchInsert([1,2,5,6], 4))

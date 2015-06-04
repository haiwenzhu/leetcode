class Solution:
    """
    https://oj.leetcode.com/problems/sort-colors/
    """
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        n = len(A)
        left = 0
        right = n-1
        while left <= right and A[left] == 0:
            left += 1
        while right >= left and A[right] == 2:
            right -= 1
        i = left 
        while i <= right:
            if A[i] == 1 or i < left:
                i += 1
                continue
            if A[i] == 0:
                tmp = A[left]
                A[left] = A[i]
                A[i] = tmp
                left += 1
                while left <= right and A[left] == 0:
                    left += 1
            elif A[i] == 2:
                tmp = A[right]
                A[right] =A[i]
                A[i] = tmp
                right -= 1
                while right >= left and A[right] == 2:
                    right -= 1
        return A
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.sortColors([1,2,0]))

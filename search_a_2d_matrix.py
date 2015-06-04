class Solution:
    """
    @see https://oj.leetcode.com/problems/search-a-2d-matrix/
    """
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        col1 = []
        for row in matrix:
            col1.append(row[0])
        n = len(col1)
        min_idx = 0
        max_idx = n - 1
        while min_idx <= max_idx:
            mid = (min_idx+max_idx) // 2
            if col1[mid] == target:
                return True
            elif col1[mid] > target:
                max_idx = mid - 1
            else:
                min_idx = mid + 1
        row = matrix[max_idx]
        min_idx = 0
        max_idx = len(row) - 1
        while min_idx <= max_idx:
            mid = (min_idx+max_idx) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                max_idx = mid - 1
            else:
                min_idx = mid + 1
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchMatrix([[1,3,4],[5,6,8],[9,10,11]], 7))

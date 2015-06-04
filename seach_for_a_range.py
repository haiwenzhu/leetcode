class Solution:
    """
    @see https://oj.leetcode.com/problems/search-for-a-range/
    """
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        n = len(A)
        min = 0
        max = n-1
        mid = -1
        while min <= max:
            mid = (min+max) // 2
            if A[mid] == target:
                break
            elif A[mid] > target:
                max = mid-1
            else:
                min = mid+1
        if mid < 0 or A[mid] != target:
            return [-1, -1]
        print(mid)
        mid1 = mid
        min = 0
        max = mid1
        res_min = res_max = mid1
        while min <= max:
            mid = (min+max) // 2
            if A[mid] < target:
                min = mid+1
            else:
                max = mid-1
                if max >= 0 and A[max] != target:
                    break
        res_min = mid

        min = mid1
        max = n - 1
        while min <= max:
            mid = (min+max) // 2
            if A[mid] > target:
                max = mid - 1
            else:
                min = mid + 1
                if min < n and A[min] != target:
                    break
        res_max = mid

        return [res_min, res_max]

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchRange([1,1], 1))

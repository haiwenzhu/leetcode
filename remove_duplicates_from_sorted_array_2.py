class Solution:
    """
    @see https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
    """
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        l = len(A)
        if l == 0:
            return 0
        loop = 1
        idx = 1
        last_num = A[0]
        last_c = 1
        while loop < l:
            if A[idx] == last_num:
                if last_c == 2:
                    del A[idx:idx+1]
                else:
                    last_c += 1
                    idx += 1
            else:
                last_num = A[idx]
                last_c = 1
                idx += 1
            loop += 1
        return len(A)

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([]))


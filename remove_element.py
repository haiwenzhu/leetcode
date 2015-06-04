class Solution:
    """
    @see https://oj.leetcode.com/problems/remove-element/
    """
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        length = len(A)
        i = 0
        while i < length:
            if A[i] == elem:
                length -= 1
                A[i] = A[length]
                A[length] = elem
            else:
                i += 1

        return length

if __name__ == "__main__":
    A = [1,2,2]
    solution = Solution()
    print(solution.removeElement(A, 2))

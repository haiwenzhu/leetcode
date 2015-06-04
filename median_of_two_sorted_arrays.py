class Solution:
    """
    @see https://oj.leetcode.com/problems/median-of-two-sorted-arrays/
    """
    # @return a float
    def findMedianSortedArrays(self, A, B):
        lena = len(A)
        lenb = len(B)
        if (lena+lenb)%2 == 0:
            return (self.findKth(A, B, (lena+lenb) // 2) + self.findKth(A, B, (lena+lenb)//2 + 1)) * 0.5
        else:
            return self.findKth(A, B, (lena+lenb+1)//2) * 1.0

    def findKth(self, A, B, k):
        lena = len(A)
        lenb = len(B)
        if lena == 0:
            return B[k-1]
        if lenb == 0:
            return A[k-1]
        if k == 1:
            return min(A[0], B[0])
        if lena < lenb:
            ka = min(k // 2, lena)
            kb = k - ka
        else:
            kb = min(k // 2, lenb)
            ka = k - kb
        if A[ka-1] < B[kb-1]:
            return self.findKth(A[ka:], B, kb)
        else:
            return self.findKth(A, B[kb:], ka)

if __name__ == "__main__":
    solution = Solution()
    print(solution.findMedianSortedArrays([1,2,3],[]))

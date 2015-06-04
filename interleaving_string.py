class Solution:
    """
    @see https://leetcode.com/problems/interleaving-string/
    """
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)
        if len1 + len2 != len3:
            return False
        arr = [[True]+[False]*len2]
        for i in range(1, len1+1):
            arr.append([False]*(len2+1))
            arr[i][0] = arr[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, len2+1):
            arr[0][j] = s2[j-1] == s3[j-1]
            if not arr[0][j]:
                break
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                arr[i][j] = (arr[i][j-1] and s2[j-1] == s3[i+j-1]) or (arr[i-1][j] and s1[i-1] == s3[i+j-1])
        return arr[len1][len2]


if __name__ == "__main__":
    solution = Solution()
    print(solution.isInterleave('cb', '', 'cb'))
    #print(solution.isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))

class Solution:
    """
    @see https://leetcode.com/problems/edit-distance/
    """
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        d = {}
        for i in range(0, len1+1):
            d[i] = {}
            for j in range(0, len2+1):
                if i > 0 and j > 0:
                    if word1[i-1] == word2[j-1]:
                        d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1])
                    else:
                        d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+1)
                elif i == 0:
                    d[i][j] = j
                else:
                    d[i][j] = i
        return d[len1][len2]

if __name__ == "__main__":
    solution =  Solution()
    print(solution.minDistance('abc', 'bc'))


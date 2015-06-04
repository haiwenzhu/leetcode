class Solution:
    """
    @see https://oj.leetcode.com/problems/implement-strstr/
    """
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        n1 = len(haystack)
        n2 = len(needle)

        if n2 == 0:
            return 0
        else:
            for i in range(0, n1-n2+1):
                if haystack[i] == needle[0] and haystack[i:i+n2] == needle:
                    return i

            return -1 

if __name__ == "__main__":
    solution = Solution()
    print solution.strStr('abc', 'b')
    print solution.strStr('', '')

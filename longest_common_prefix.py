class Solution:
    """
    @see https://oj.leetcode.com/problems/longest-common-prefix/
    """
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        idx = 0
        try:
            while True:
                for i in range(1, len(strs)):
                    if strs[i][idx] != strs[0][idx]:
                        return strs[0][0:idx]
                idx += 1
        except IndexError:
            return strs[0][0:idx]
                
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["abc", "abd", "abe"]))
    print(solution.longestCommonPrefix(["aa", "aa"]))
    print(solution.longestCommonPrefix(["a", "a", "b"]))
    print(solution.longestCommonPrefix(["abc"]))
    print(solution.longestCommonPrefix([]))
        


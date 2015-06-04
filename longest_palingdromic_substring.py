class Solution:
    """
    @see https://oj.leetcode.com/problems/longest-palindromic-substring/
    """
    # @return a string
    def longestPalindrome(self, s):
        n = len(s)
        maxlen  = 1 if n>0 else 0
        idx = 0

        for i in range(1, n):
            l = i
            r = i
            if s[i] == s[i-1]:
                l = i-1
                r = i
                while l-1 >= 0 and r+1 < n and s[l-1] == s[r+1]:
                    l -= 1
                    r += 1
                if maxlen < r-l+1:
                    maxlen = r-l+1
                    idx = l
            if i+1 < n and s[i+1] == s[i-1]:
                l = i-1
                r = i+1
                while l-1 >= 0 and r+1 < n and s[l-1] == s[r+1]:
                    l -= 1
                    r += 1
                if maxlen < r-l+1:
                    maxlen = r-l+1
                    idx = l

        return s[idx:idx+maxlen]

                 
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("aaabaaaa"))

class Solution:
    """
    @see https://oj.leetcode.com/problems/length-of-last-word/
    """
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        n = len(s)-1
        while n >= 0 and s[n] != ' ':
            n -= 1
        return len(s) - n - 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLastWord("hello world"))
    print(solution.lengthOfLastWord("hello world "))
    print(solution.lengthOfLastWord(""))

        


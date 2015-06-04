class Solution:
    """
    @see https://oj.leetcode.com/problems/palindrome-number/
    """
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False

        t = x
        y = 0
        while t > 0:
            y = y*10 + (t%10)
            t //= 10

        return x == y

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(121))
    print(solution.isPalindrome(-121))
    print(solution.isPalindrome(-12100))


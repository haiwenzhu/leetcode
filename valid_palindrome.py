class Solution:
    """
    @see https://oj.leetcode.com/problems/valid-palindrome/
    """
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        str = [c for c in s.lower() if (c >= '0' and c <= '9') or (c >= 'a' and c <= 'z')]
        for i in range(0, len(str)):
            if str[i] != str[-1-i]:
                return False
        
        return True


if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome("A man, a plan, a canal: Panama"))
    print(obj.isPalindrome("race a car"))

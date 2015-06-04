class Solution:
    """
    @see https://oj.leetcode.com/problems/string-to-integer-atoi/
    """
    # @return an integer
    def atoi(self, str):
        s = 0
        sign = 0
        for i,c in enumerate(str):
            if sign == 0 and c == ' ':
                continue
            if sign == 0 and (c == '-' or c == '+'):
                sign = -1 if c == '-' else 1
            elif c >= '0' and c <= '9':
                s = s*10 + int(c)
                if sign == 0:
                    sign = 1
            else:
                break
        s *= sign
        if s > 2**31-1:
            return 2**31-1
        elif s < -2**31:
            return -2**31
        else:
            return s

if __name__ == "__main__":
    solution = Solution()
    print(solution.atoi("   -1  2x"))
    print(solution.atoi("   12+12"))
    print(solution.atoi("2147483648"))
    print(solution.atoi(""))

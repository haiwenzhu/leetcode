class Solution:
    """
    @see https://oj.leetcode.com/problems/plus-one/
    """
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        n = len(digits)
        f = 1
        res = []
        for i in range(n):
            if f == 0:
                res[0:0] = digits[0:-i]
                break
            if digits[-i-1] + f >= 10:
                f = 1
                res[0:0] = [0]
            else:
                res[0:0] = [digits[-i-1] + f]
                f = 0
        if f == 1:
            res[0:0] = [f]
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([9,9,9]))

        

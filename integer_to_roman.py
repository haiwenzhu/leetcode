class Solution:
    """
    @see https://oj.leetcode.com/problems/integer-to-roman/
    """
    # @return a string
    def intToRoman(self, num):
        chart = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        roman = ''
        if num >= 1000:
            roman += chart[1000]*(num//1000)
            num %= 1000
        for s in [100, 10, 1]:
            if num >= 9*s:
                roman += chart[s] + chart[10*s]
            elif num >= 5*s:
                num -= 5*s
                roman += chart[5*s] + chart[s]*(num//s)
            elif num >= 4*s:
                roman +=chart[s] + chart[5*s]
            elif num >= s:
                roman += chart[s] * (num//s)
            num %= s
        
        return roman

if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(1234))
    print(solution.intToRoman(35))

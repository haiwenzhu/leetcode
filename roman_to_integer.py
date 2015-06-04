class Solution:
    """
    @see https://oj.leetcode.com/problems/roman-to-integer/
    """
    # @return an integer
    def romanToInt(self, s):
        chart = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        if s == "":
            return 0

        n = chart[s[-1]]
        for i in range(2, len(s)+1):
            if chart[s[-i]] < chart[s[-i+1]]:
                n -= chart[s[-i]]
            else:
                n += chart[s[-i]]
        
        return n

if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt(""))
    print(solution.romanToInt("VII") == 7)
    print(solution.romanToInt("XXXIX") == 39)
    print(solution.romanToInt("DCCCXC") == 890)

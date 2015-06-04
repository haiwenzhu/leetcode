class Solution:
    """
    @see https://oj.leetcode.com/problems/zigzag-conversion/
    """
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        str = ""
        l = len(s)
        for row in range(nRows):
            if row == 0 or row == nRows-1:
                for i in range(row, l, 2*nRows-2):
                    str += s[i]
            else:
                end = nRows-1
                i = row
                while i < l:
                    str += s[i]
                    i = i + abs(row-end)*2
                    end = nRows-1-end

        return str
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
    print(solution.convert("AB", 1) == "AB")
    print(solution.convert("ABCDE", 2) == "ACEBD")

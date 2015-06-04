class Solution:
    """
    @see https://oj.leetcode.com/problems/add-binary/
    """
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        la = len(a)
        lb = len(b)
        minl = min(la, lb)
        maxl = max(la, lb)
        longstr = a if maxl == la else b
        i = 1
        f = "0"
        res = ""
        while i <= minl:
            if a[-i] == "1" and b[-i] == "1":
                res = f + res
                f = "1"
            elif a[-i] == "1" or b[-i] == "1":
                if f == "1":
                    res = "0" + res
                else:
                    res = "1" + res
            else:
                res = f + res
                f = "0"
            i += 1
        while i <=  maxl:
            if f == "0":
                res = longstr[0:-i+1] + res
                break
            elif longstr[-i] == "1":
                res = "0" + res
            else:
                res = "1" + res
                f = "0"
            i += 1
        if f == "1":
            res = "1" + res
        return res
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.addBinary("100", "110010"))


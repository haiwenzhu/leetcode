class Solution:
    """
    @see https://leetcode.com/problems/valid-number/
    """
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        s = s.strip()
        floatpoint = False
        exp = False
        num = False
        lastc = ''
        for c in s:
            if c == '+' or c == '-':
                if lastc != '' and lastc != 'e':
                    return False
            elif c == '.':
                if not floatpoint and not exp:
                    floatpoint = True
                else:
                    return False
            elif c == 'e':
                if num and not exp:
                    exp = True
                    num = False
                else:
                    return False
            elif c >= '0' and c <= '9':
                if not num:
                    num = True
            else:
                return False
            lastc = c
        return num

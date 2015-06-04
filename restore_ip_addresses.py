class Solution:
    """
    @see https://oj.leetcode.com/problems/restore-ip-addresses/
    """
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        return self._restore(s, '', len(s), 4)
        
    def _restore(self, s, s1, l, c):
        res = []
        if c == 1:
            if (l == 1 or s[0] != '0') and int(s) <= 255:
                res.append(s1 + '.' + s)
        elif c == 4:
            if l > 3 and s[0] != '0' and int(s[0:3]) <= 255:
                res.extend(self._restore(s[3:], s[0:3], l-3, c-1))
            if l > 2 and s[0] != '0':
                res.extend(self._restore(s[2:], s[0:2], l-2, c-1))
            if l > 1:
                res.extend(self._restore(s[1:], s[0:1], l-1, c-1))
        else:
            if l > 3 and s[0] != '0' and int(s[0:3]) <= 255:
                res.extend(self._restore(s[3:], s1+'.'+s[0:3], l-3, c-1))
            if l > 2 and s[0] != '0':
                res.extend(self._restore(s[2:], s1+'.'+s[0:2], l-2, c-1))
            if l > 1:
                res.extend(self._restore(s[1:], s1+'.'+s[0:1], l-1, c-1))
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.restoreIpAddresses("010010"))

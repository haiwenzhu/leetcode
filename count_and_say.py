class Solution:
    """
    @see https://oj.leetcode.com/problems/count-and-say/
    """
    # @return a string
    def countAndSay(self, n):
        s = "1"
        while n > 1:
            s = self._next(s)
            n -= 1

        return s

    def _next(self, s):
        pre = ''
        count = 0
        s1 = ""
        for c in s:
            if pre != c:
                if count > 0:
                    s1 += str(count) + pre
                pre = c
                count = 1
            else:
                count += 1
        s1 += str(count) + pre
        return s1

if __name__ == "__main__":
    solution = Solution()
    for i in range(1, 20):
        print(solution.countAndSay(i))

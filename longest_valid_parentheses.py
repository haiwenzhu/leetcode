class Solution:
    """
    @see https://leetcode.com/problems/longest-valid-parentheses/
    """
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        idx_arr = []
        s = s.lstrip(')')
        lastidx = -1
        idx = []
        max = 0
        for i in range(0, len(s)):
            if s[i] == ')':
                if lastidx >= 0:
                    idx_arr.append(lastidx)
                    idx_arr.append(i)
                    lastidx = -1
                elif len(idx) > 0:
                    idx_arr.append(idx.pop())
                    idx_arr.append(i)
            else:
                if lastidx >= 0:
                    idx.append(lastidx)
                lastidx = i
        if len(idx_arr) > 0:
            idx_arr = sorted(idx_arr)
            pre = -2
            n = 1
            for i in idx_arr:
                if i - pre == 1:
                    n += 1
                else:
                    max = n if max < n else max
                    n = 1
                pre = i
            max = n if max < n else max
        return max
            

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestValidParentheses("("))
                
        

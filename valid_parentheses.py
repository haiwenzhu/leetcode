import collections

class Solution:
    """
    @see https://oj.leetcode.com/problems/valid-parentheses/
    """
    # @return a boolean
    def isValid(self, s):
        q = collections.deque()
        for c in s:
            if len(q) > 0:
                c1 = q.pop()
                if (c1=="(" and c!=")") \
                    or (c1=="{" and c!="}") \
                    or (c1=="[" and c!="]"):
                    q.extend([c1, c])
            else:
                q.append(c)

        return len(q) == 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("(){}[()]"));
    print(solution.isValid("()"));


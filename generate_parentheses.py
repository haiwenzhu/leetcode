import collections
class Solution:
    """
    @see https://oj.leetcode.com/problems/generate-parentheses/
    """
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        q = collections.deque([("", 0, 0)])
        res = []
        while q:
            item = q.popleft()
            if item[1] == n and item[2] == n:
                res.append(item[0])
            if item[1] > item[2]:
                if item[1] < n:
                    q.append((item[0]+"(", item[1]+1, item[2]))
                q.append((item[0]+")", item[1], item[2]+1))
            else:
                if item[1] < n:
                    q.append((item[0]+"(", item[1]+1, item[2]))
        return res
            

if __name__ == "__main__":
    solution = Solution()
    res = solution.generateParenthesis(4)
    res1 = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
    for item in res1:
        if res.count(item) != 1:
            print(item)

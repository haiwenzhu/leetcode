class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res = [[]]
        S = sorted(S)
        for n in S:
            for item in res[0:]:
                t = item[0:]
                t.append(n)
                if t not in res:
                    res.append(t)
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.subsetsWithDup([1,2,2]))

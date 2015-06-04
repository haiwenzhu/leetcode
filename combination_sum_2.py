class Solution:
    """
    @see https://oj.leetcode.com/problems/combination-sum-ii/
    """
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        res = []
        candidates = sorted(candidates)
        if len(candidates) == 0:
            return res
        comb = [[]]
        for num in candidates:
            if num > target:
                continue
            comb1 = [] 
            for item in comb:
                comb1.append(item[0:])
                tmp = item[0:]
                tmp.append(num)
                s = sum(tmp)
                if s < target:
                    comb1.append(tmp)
                elif s == target and tmp not in res:
                    res.append(tmp)
            comb = comb1

        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum2([11,10,14,12,34,31,27,34,13,6,24,22,21,27,34,5,21,5,25,12,15,24,11,34,29,22,28,19,31,34,5,29,31,14,7,31,10,21,22,10,23,11,20,31,25,11,31,34,11,21,11,22,10,17], 28))

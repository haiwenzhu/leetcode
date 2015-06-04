class Solution:
    """
    @see https://oj.leetcode.com/problems/combination-sum/
    """
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        comb = []
        res = []
        candidates = sorted(candidates)
        n = len(candidates)
        for num in candidates:
            max = target // num
            if len(comb) == 0:
                for i in range(0, max):
                    comb.append([num]*i)
                if max*num == target:
                    res.append([num]*max)
            else:
                comb1 = [] 
                for i in range(0, max+1):
                    for item in comb:
                        tmp = item[0:]
                        tmp.extend([num]*i)
                        s = sum(tmp)
                        if s < target:
                            comb1.append(tmp)
                        elif s == target:
                            res.append(tmp)
                comb = comb1

        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum([1], 1))


        


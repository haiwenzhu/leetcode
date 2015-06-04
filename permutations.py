class Solution:
    """
    @see https://oj.leetcode.com/problems/permutations/
    """
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        if len(num) == 0:
            return []
        res = [[]]
        l = 0
        for n in num:
            res1 = []
            for item in res:
                for i in range(l, -1, -1):
                    item1 = item[0:]
                    item1[i:i] = [n]
                    res1.append(item1)
            res = res1
            l += 1
        return res
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.permute([1,2,3]))

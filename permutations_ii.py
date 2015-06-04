class Solution:
    """
    @see https://leetcode.com/problems/permutations-ii/
    """
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        if len(num) == 0:
            return []
        res = [[num.pop(0)]]
        l = 1
        map = {}
        for n in num:
            res1 = []
            for item in res:
                for i in range(l, -1, -1):
                    item1 = item[0:]
                    item1[i:i] = [n]
                    s = str(item1)
                    if s not in map:
                        map[s] = 1
                        res1.append(item1)
            res = res1
            l += 1
        return res
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.permuteUnique([1,2,2]))

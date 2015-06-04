class Solution:
    """
    @see https://oj.leetcode.com/problems/3sum/
    """
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        l = len(num)
        res = []
        map = {}
        for i in range(0, l-1):
            for j in range(i+1, l):
                sumij = num[i] + num[j]
                sumleft = target - sumij
                if sumleft in map:
                    for (m,n) in map[sumleft]:
                        if n<i and [num[m], num[n], num[i], num[j]] not in res:
                            res.append([num[m], num[n], num[i], num[j]])
                if sumij in map:
                    map[sumij].append((i,j))
                else:
                    map[sumij] = [(i,j)]
        return res 

if __name__ == "__main__":
    solution = Solution()
    print(solution.fourSum([0,0,0,0], 0))
    #print(solution.fourSum([-477,-476,-471,-462,-440,-400,-398,-394,-394,-393,-389,-386,-350,-346,-338,-315,-273,-249,-182,-172,-166,-161,-149,-116,-112,-109,-100,-73,-33,-26,-22,-11,6,8,13,19,56,78,101,102,111,140,155,158,181,205,211,225,232,242,254,265,281,308,310,320,320,364,366,381,385,387,443,496,496], 1236))


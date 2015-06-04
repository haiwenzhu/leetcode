class Solution:
    """
    @see https://oj.leetcode.com/problems/combinations/
    """
    # @return a list of lists of integers
    def combine(self, n, k):
        d = {}
        for i in range(k):
            d[i+1] = []
        for num in range(1, n+1):
            for i in range(1, k):
                items = d[k-i]
                for item in items:
                    t = item[0:]
                    t.append(num)
                    d[k-i+1].append(t)
            d[1].append([num])
        return d[k]

if __name__ == "__main__":
    solution = Solution()
    print(solution.combine(3, 3))

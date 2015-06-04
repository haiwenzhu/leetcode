class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        res = 0
        sign1 = 1 if dividend >= 0 else -1
        sign2 = 1 if divisor >= 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        l1 = []
        l2 = []
        t1 = divisor
        t2 = 0 
        while t1 <= dividend:
            if t2 == 0:
                t2 = 1
            l1.append(t1)
            l2.append(t2)
            t1 += t1
            t2 += t2
        for i in reversed(range(len(l2))):
            if dividend >= l1[i]:
                res += l2[i]
                dividend -= l1[i]

        res = res if sign1==sign2 else -res
        if res < -2147483648 or res > 2147483647:
            res = 2147483647
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.divide(0,1))

class Solution:
    """
    @see https://oj.leetcode.com/problems/multiply-strings/
    """
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        #return str(int(num1)*int(num2))
        list1 = []
        list2 = []
        for i in num1:
            list1.append(int(i))
        for i in num2:
            list2.append(int(i))
        res = []
        l1 = len(list1)
        l2 = len(list2)
        l = 0
        for i in range(l1):
            m = list1[-1-i]
            f = 0
            for j in range(l2):
                n = list2[-1-j]
                if l > i+j:
                    res[i+j] += n*m+f
                else:
                    res.append(n*m+f)
                    l += 1
                if res[i+j] >= 10:
                    f = res[i+j] // 10
                    res[i+j] %= 10
                else:
                    f = 0
            if f > 0:
                res.append(f)
                l += 1
        if l > 0 and res[-1] == 0:
            return "0";
        else:
            return ''.join([str(i) for i in reversed(res)])

        
if __name__ == "__main__":
    solution = Solution()
    print(solution.multiply('123', '456'))

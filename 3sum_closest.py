class Solution:
    """
    @see https://oj.leetcode.com/problems/3sum-closest/
    """
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        l = len(num)
        res = num[0] + num[1] + num[2] - target
        res_abs = abs(res)
        for i in range(0, l-2):
            num_i = num[i]
            if i > 0 and num_i == num[i-1]:
                continue
            j, k = i+1, l-1
            while j < k:
                num_j = num[j]
                num_k = num[k]
                s = num_i + num_j + num_k - target
                if res_abs > abs(s):
                    res = s
                    res_abs = abs(res)
                if s == 0:
                    return res + target
                elif s > 0:
                    k -= 1
                    while j < k and num[k] == num[k+1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and num[j] == num[j-1]:
                        j += 1

        return res + target
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumClosest([0,2,1,-3], 1))


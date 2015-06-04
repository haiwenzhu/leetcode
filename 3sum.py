class Solution:
    """
    @see https://oj.leetcode.com/problems/3sum/
    """
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        l = len(num)
        res = []
        for i in range(0, l-2):
            num_i = num[i]
            if i > 0 and num_i == num[i-1]:
                continue
            j, k = i+1, l-1
            while j < k:
                num_j = num[j]
                num_k = num[k]
                s = num_i + num_j + num_k
                if s == 0:
                    res.append([num_i, num_j, num_k])
                    j += 1
                    while j < k and num[j] == num[j-1]:
                        j += 1
                    k -= 1
                    while j < k and num[k] == num[k+1]:
                        k -= 1
                elif s > 0:
                    k -= 1
                    while j < k and num[k] == num[k+1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and num[j] == num[j-1]:
                        j += 1

        return res
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
    print(solution.threeSum([1,-1,-1,0]))


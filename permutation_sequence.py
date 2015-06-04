import math
class Solution:
    """
    @see https://oj.leetcode.com/problems/permutation-sequence/
    """
    # @return a string
    def getPermutation(self, n, k):
        fct = 1
        nums = [str(i) for i in range(1, n+1)]
        for i in range(1, n+1):
            fct *= i
        res = []
        for i in range(0, n):
            fct /= (n-i)
            idx = int(math.ceil(float(k) / fct)) - 1
            res.append(nums[idx])
            del nums[idx:idx+1]
            k %= fct
            if k == 0:
                res.extend(reversed(nums))
                break
            elif k == 1:
                res.extend(nums)
                break
        return "".join(res)
       
if __name__ == "__main__":
    solution = Solution()
    print(solution.getPermutation(3,1))

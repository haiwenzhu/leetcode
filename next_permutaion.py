class Solution:
    """
    @see https://oj.leetcode.com/problems/next-permutation/
    """
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        n = len(num)
        #keep the right side of the pivot in asc order
        #find the smallest number in right side of the pivot which larger than the pivot
        #and then swap them
        for i in reversed(range(n-1)):
            tmp = num[i]
            if num[i] >= num[n-1]:
                for j in range(i, n-1):
                    num[j] = num[j+1]
                num[n-1] = tmp
            else:
                for j in range(i+1, n):
                    if num[j] > tmp:
                        num[i] = num[j]
                        num[j] = tmp
                        break
                break
        return num

if __name__ == "__main__":
    solution = Solution()
    print(solution.nextPermutation([1,2,3]))
    print(solution.nextPermutation([1]))
    print(solution.nextPermutation([1,1]))

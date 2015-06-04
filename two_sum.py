class Solution:
    """
    @see https://oj.leetcode.com/problems/two-sum/
    """
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        num1 = sorted(num)
        i = 0;
        j = len(num) - 1
        while i < j:
            if num1[i] + num1[j] == target:
                index_i = num.index(num1[i]) + 1
                index_j = num.index(num1[j], index_i)+1 if num1[i]==num1[j] else num.index(num1[j])+1
                return (index_i, index_j) if index_i<index_j else (index_j, index_i)
            elif num1[i] + num1[j] > target:
                j -= 1
            else:
                i += 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))
    print(solution.twoSum([2,1,9,4,4,56,90,3], 8))

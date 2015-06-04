class Solution:
    """
    @see https://oj.leetcode.com/problems/pascals-triangle/
    """
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows <= 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            lists = [[1],[1,1]]
            for i in range(2, numRows):
                item = [1]
                for j in range(1, len(lists[i-1])):
                    item.append(lists[i-1][j-1] + lists[i-1][j])
                item.append(1)
                lists.append(item)
            return lists

if __name__ == "__main__":
    solution = Solution()
    print(solution.generate(5))
        

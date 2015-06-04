class Solution:
    """
    @see https://oj.leetcode.com/problems/pascals-triangle/
    """
    # @return a list of lists of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            lists = [1,1]
            while rowIndex > 1:
                item = [1]
                for j in range(1, len(lists)):
                    item.append(lists[j-1] + lists[j])
                item.append(1)
                lists = item
                rowIndex -= 1
            return lists

if __name__ == "__main__":
    solution = Solution()
    print(solution.getRow(5))
        

class Solution:
    """
    @see https://leetcode.com/problems/maximal-rectangle/
    """
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        maxarea = 0
        rlen = len(matrix)
        if rlen == 0 or len(matrix[0]) == 0:
            return maxarea
        arr = []
        for i,row in enumerate(matrix):
            num = int(''.join(row), 2)
            for j,n in enumerate(arr):
                arr[j] &= num
                if arr[j]*(i-j+1) > maxarea:
                    area = self.maxSequence1(arr[j])*(i-j+1)
                    maxarea = area if area > maxarea else maxarea
            arr.append(num)
            area = self.maxSequence1(num)
            maxarea = area if area > maxarea else maxarea
        return maxarea

    #the max length of sequence num 1
    def maxSequence1(self, num):
        max_s1 = 0
        s1 = 0
        while num > 0:
            if num%2 == 1:
                s1 += 1
            else:
                max_s1 = s1 if max_s1 < s1 else max_s1
                s1 = 0
            num //= 2
        max_s1 = s1 if max_s1 < s1 else max_s1
        return max_s1


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximalRectangle([['1','1'],['1','1']]))
    print(solution.maximalRectangle(["10100","10111","11111","10010"]))

        


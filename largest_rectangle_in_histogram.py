class Solution:
    """
    @see https://leetcode.com/problems/largest-rectangle-in-histogram/
    """
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        rec = []
        pre = -1 
        n = len(height)
        if n == 0:
            return 0
        l = 0
        largest = 0
        for i,v in enumerate(height):
            temprec = [v, -1, i]
            if v > pre:
                rec.append([v, i, i])
                l += 1
            else:
                j = 0
                exist = False
                while j < l:
                    if rec[j][0] > v:
                        largest1 = rec[j][0]*(i - rec[j][1])
                        largest = largest1 if largest1 > largest else largest
                        if temprec[1] < 0:
                            temprec[1] = rec[j][1]
                        rec.pop(j)
                        l -= 1
                    else:
                        if rec[j][0] == v:
                            exist = True
                        rec[j][2] = i
                        j += 1
                if not exist:
                    rec.append(temprec)
                    l += 1
            pre = v 
        i = l-2
        while i >= 0:
            rec[i][2] = rec[i+1][2]
            i -= 1
        for item in rec:
            largest1 = item[0]*(item[2]-item[1]+1)
            largest = largest1 if largest1 > largest else largest

        return largest 


if __name__ == "__main__":
    solution = Solution()
    print(solution.largestRectangleArea([2,1,5,6,2,3]))
    #print(solution.largestRectangleArea([5,4,1,2]))
    #print(solution.largestRectangleArea([]))
    #print(solution.largestRectangleArea([0,9]))

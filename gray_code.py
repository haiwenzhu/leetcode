class Solution:
    """
    @see https://oj.leetcode.com/problems/gray-code/
    """
    # @return a list of integers
    def grayCode(self, n):
        n2 = [2**i for i in range(n)]
        nums = [i for i in range(1, 2**n)]
        res = [0]
        lastNum = 0
        print(n2)
        while len(nums) > 0:
            lastNum1 = lastNum
            for num in n2:
                #when plus, turn bit 0->1
                if lastNum+num in nums and num & lastNum == 0:
                    lastNum += num
                    res.append(lastNum)
                    nums.remove(lastNum)
                    break
                #when minus turn bit 1->0
                elif lastNum-num in nums and num & lastNum == num:
                    lastNum -= num
                    res.append(lastNum)
                    nums.remove(lastNum)
                    break
            if lastNum1 == lastNum:
                break
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.grayCode(3))

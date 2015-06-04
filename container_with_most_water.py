class Solution:
    """
    @see https://oj.leetcode.com/problems/container-with-most-water/
    """
    # @return an integer
    def maxArea(self, height):
        i, j = 0, len(height)-1
        h = max(height[i], height[j])
        l = min(height[i], height[j])
        m = j*l
        while i < j:
            if height[i] < h or height[j] < h:
                l1 = min(height[i], height[j])
                if l1 > l:
                    m1 = l1*(j-i)
                    m = m1 if m < m1 else m
                    l1 = l
                if height[i] < h:
                    i += 1
                else:
                    j -= 1
            else:
                l = h
                h = max(height[i], height[j])
                m1 = l*(j-i)
                m = m1 if m1>m else m
                if height[i] < h:
                    i += 1
                else:
                    j -= 1

        return m

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([2,5,4,5,2]))

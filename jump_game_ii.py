class Solution:
    """
    @see https://leetcode.com/problems/jump-game-ii/
    """
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        n = len(nums)
        jump = 0
        st = 0
        i = st + 1
        while i < n:
            end = -1 
            while i < n and i-st<=nums[st]:
                if end < 0:
                    end = i
                elif nums[end]+end <= nums[i]+i:
                    end = i
                i += 1
            if end > 0:
                st = end
                jump += 1
            elif end < 0:
                return -1
        return jump


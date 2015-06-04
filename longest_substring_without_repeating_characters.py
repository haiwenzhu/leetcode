class Solution:
    """
    @see https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/
    """
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        maxlen = 0
        l = len(s)
        charindex = {}
        startindex = 0
        for i in range(l):
            if s[i] not in charindex:
                charindex[s[i]] = i
                maxlen = max(maxlen, i-startindex+1)
            else:
                startindex = max(startindex, charindex[s[i]]+1)
                charindex[s[i]] = i
                maxlen = max(maxlen, i-startindex+1)

        return maxlen
                
                
if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbb"))
    print(solution.lengthOfLongestSubstring(""))

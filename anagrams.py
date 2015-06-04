class Solution:
    """
    @see https://oj.leetcode.com/problems/anagrams/
    """
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        d = {}
        for str in strs:
            str1 = sorted(str)
            str1 = "".join(str1)
            if str1 not in d:
                d[str1] = [str]
            else:
                d[str1].append(str)
        res = []
        for v in d.values():
            if len(v) > 1:
                res.extend(v)
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.anagrams(["abc", "acb", "aaa", "abd", "dba"]))

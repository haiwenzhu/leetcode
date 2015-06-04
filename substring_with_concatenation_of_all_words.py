class Solution:
    """
    @see https://leetcode.com/problems/substring-with-concatenation-of-all-words/
    """
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        l = len(L[0])
        lenOfL = len(L)
        res = []
        for i in range(0, l):
            matches = []
            for j in range(i, len(S), l):
                s = S[j:j+l]
                if s in L:
                    if matches.count(s) != L.count(s):
                        matches.append(s)        
                        if len(matches) == lenOfL:
                            res.append(j - lenOfL*l + l)
                            matches.pop(0)
                    else:
                        #delete the part befor first occurance of s
                        tmp = matches[matches.index(s)+1:]
                        matches = tmp
                        matches.append(s)
                else:
                    matches = []
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.findSubstring("abababab", ["a", "b", "a"]))

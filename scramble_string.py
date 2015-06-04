class Solution:
    """
    @see https://leetcode.com/problems/scramble-string/
    """
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        length = len(s1)
        i = j = 0
        idx_arr = []
        flag = False
        while i < length or j < length:
            if j < length and s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                try:
                    if not flag:
                        j1 = s2.index(s1[i], j)
                        idx_arr.append((i, j, j1))
                        j = j1
                        flag = True
                    else:
                        idx = idx_arr[-1]
                        if self.isScramble(s1[i:i+idx[2]-idx[1]], s2[idx[1]:idx[2]]):
                            i = j
                            flag = False
                        else:
                            raise ValueError
                except ValueError:
                    while idx_arr:
                        idx = idx_arr.pop()
                        j1 = s2.find(s1[idx[0]], idx[2]+1)
                        if idx[2] > 0:
                            i = idx[0]
                            idx_arr.append((i, idx[1], j1))
                            j = j1
                            break
                    else:
                        break
        return i == j and i == length
                    
if __name__ == "__main__":
    solution = Solution()
    print(solution.isScramble("great", "rgtea"))
    print(solution.isScramble("great", "rgtaa"))
    print(solution.isScramble("abcd", "dacb"))

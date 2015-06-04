class Solution:
    """
    @see https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/
    """
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        map = {
            "0": [''],
            "1": [''],
            "2": ['a','b','c'],
            "3": ['d','e','f'],
            "4": ['g','h','i'],
            "5": ['j','k','l'],
            "6": ['m','n','o'],
            "7": ['p','q','r','s'],
            "8": ['t','u','v'],
            "9": ['w','x','y','z'],
        }
        res = []
        n = len(digits)

        if n == 0:
            return [""]
        elif n == 1:
            return map[digits[n-1]]
        else:
            lists = self.letterCombinations(digits[0:n-1])
            for c in map[digits[n-1]]:
                for s in lists:
                    res.append(s+c)
            return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations(""))

        
        

